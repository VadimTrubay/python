import pickle
import redis
from typing import Optional

from jose import JWTError, jwt
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from pydantic import EmailStr

from contacts.database.db import get_db
from contacts.database.models import User
from contacts.repository import auth as repository_users
from contacts.conf.config import settings


class Auth:
    """
    class for user verification\n
    Methods: verify_password, get_password_hash, create_access_token,
    create_refresh_token, decode_refresh_token, get_current_user,
    get_email_from_token, create_email_token
    """
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    SECRET_KEY = "secret_key"
    ALGORITHM = "HS256"
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")
    r = redis.Redis(host=settings.redis_host, port=settings.redis_port, db=0)

    def verify_password(self, plain_password, hashed_password) -> bool:
        """
        The verify_password function takes a plain-text password and hashed
        password as arguments. It then uses the pwd_context object to verify that the
        plain-text password matches the hashed one.

        :param self: Make the method work for a specific instance of the class
        :param plain_password:  str: Check if the password entered by the user matches the hashed_password
        :param hashed_password:  str: Check if the password is correct
        :return: A boolean value
        """
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str) -> str:
        """
        The get_password_hash function takes a password as an argument and returns the hashed version of that password.
        The hash is generated using the pwd_context object's hash method, which uses bcrypt to generate a secure hash.

        :param self: Represent the instance of the class
        :param password: str: Take in the password that is being hashed
        :return: A hash of the password
        """
        return self.pwd_context.hash(password)

    async def create_access_token(self, data: dict, expires_delta: Optional[float] = None) -> str:
        """
        The create_access_token function creates a new access token.
            Args:
                data (dict): A dictionary containing the claims to be encoded in the JWT.
                expires_delta (Optional[float]): An optional parameter specifying how long, in seconds,
                from now that this token should expire. If not specified, it will default to 30 minutes from now.

        :param self: Refer to the current instance of the class
        :param data: dict: Pass in the data to be encoded into the jwt
        :param expires_delta: Optional[float]: Set the expiration time of the access token
        :return: An encoded access token
        """

        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + timedelta(seconds=expires_delta)
        else:
            expire = datetime.utcnow() + timedelta(minutes=30)
        to_encode.update({"iat": datetime.utcnow(), "exp": expire, "scope": "access_token"})
        encoded_access_token = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_access_token

    async def create_refresh_token(self, data: dict, expires_delta: Optional[float] = None) -> str:
        """
        The create_refresh_token function creates a refresh token for the user.
            Args:
                data (dict): A dictionary containing the user's id and username.
                expires_delta (Optional[float]): The time in seconds until the refresh token expires. Defaults to None, which is 7 days from creation date.

        :param self: Represent the instance of the class
        :param data: dict: Pass the user's data to the function
        :param expires_delta: Optional[float]: Set the expiration time of the refresh token
        :return: A string encoded token
        """
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + timedelta(seconds=expires_delta)
        else:
            expire = datetime.utcnow() + timedelta(days=7)
        to_encode.update({"iat": datetime.utcnow(), "exp": expire, "scope": "refresh_token"})
        encoded_refresh_token = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_refresh_token

    async def decode_refresh_token(self, refresh_token: str) -> EmailStr:
        """
        The decode_refresh_token function is used to decode the refresh token.
        It takes in a refresh_token as an argument and returns the email of the user if successful.
        If it fails, it raises an HTTPException with status code 401 (UNAUTHORIZED) and detail message 'Could not validate credentials'.


        :param self: Represent the instance of a class
        :param refresh_token: str: Pass in the refresh token that was sent to the client
        :return: EmailStr | HTTPException: email or Exception message
        """
        try:
            payload = jwt.decode(refresh_token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            if payload['scope'] == 'refresh_token':
                email = payload['sub']
                return email
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid scope for token')
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate credentials')

    async def get_current_user(self, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
        """
        The get_current_user function is a dependency that will be used in the
            protected endpoints. It takes a token as an argument and returns the user
            associated with that token. If no user is found, it raises an exception.

        :param self: Access the class attributes
        :param token: str: Pass the token to the function
        :param db: Session: Get the database session
        :return: User | HTTPException: user or Exception message
        """
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

        try:
            # Decode JWT
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            if payload['scope'] == 'access_token':
                email = payload["sub"]
                if email is None:
                    raise credentials_exception
            else:
                raise credentials_exception
        except JWTError as e:
            raise credentials_exception

        user = self.r.get(f"user:{email}")
        if user is None:
            user = await repository_users.get_user_by_email(email, db)
            if user is None:
                raise credentials_exception
            self.r.set(f"user:{email}", pickle.dumps(user))
            self.r.expire(f"user:{email}", 900)
        else:
            user = pickle.loads(user)
        return user

    async def get_email_from_token(self, token: str) -> EmailStr:
        """
        The get_email_from_token function takes a token as an argument and returns the email address associated with that token.
        The function uses the jwt library to decode the token, which is then used to retrieve the email address from its payload.

        :param self: Represent the instance of a class
        :param token: str: Decode the token and get the email address from it
        :return: EmailStr | HTTPException: email or Exception message
        """
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            email = payload["sub"]
            return email
        except JWTError as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                detail="Invalid token for email verification")

    def create_email_token(self, data: dict) -> str:
        """
        The create_email_token function takes a dictionary of data and returns a token.
        The token is created using the JWT library, which uses the SECRET_KEY and ALGORITHM to create an encoded string.
        The data dictionary contains information about the user's email address, as well as when it was issued (iat) and when it expires (exp).


        :param self: Represent the instance of the class
        :param data: dict: Pass in the data that will be encoded into the token
        :return: A token that is encoded using the jwt library
        """
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(days=1)
        to_encode.update({"iat": datetime.utcnow(), "exp": expire})
        token = jwt.encode(to_encode, self.SECRET_KEY,
                           algorithm=self.ALGORITHM)
        return token


auth_service = Auth()
