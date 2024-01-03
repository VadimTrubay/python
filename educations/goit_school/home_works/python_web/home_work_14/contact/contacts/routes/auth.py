from fastapi import APIRouter, HTTPException, Depends, status, Security, BackgroundTasks, Request
from fastapi.security import OAuth2PasswordRequestForm, HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from contacts.database.db import get_db
from contacts.schemas import UserModel, UserResponse, TokenModel, RequestEmail
from contacts.repository import auth as repository_auth
from contacts.services.auth import auth_service
from contacts.services.email import send_email

router = APIRouter(prefix='/auth', tags=["auth"])
security = HTTPBearer()


@router.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def signup(body: UserModel, background_tasks: BackgroundTasks,
    request: Request, db: Session = Depends(get_db)) -> dict | HTTPException:
    """
    The signup function creates a new user in the database.
        It takes a UserModel object as input and returns an HTTP response with the newly created user's information.
        If there is already an account associated with that email, it will return a 409 Conflict error.

    :param body: UserModel: Get the user's email and password
    :param db: Session: Get the database session
    :return: A dict with the user and a detail message
    :rtype: User | HTTPException
    """
    exist_user = await repository_auth.get_user_by_email(body.email, db)
    if exist_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Account already exists")
    body.password = auth_service.get_password_hash(body.password)
    new_user = await repository_auth.create_user(body, db)
    background_tasks.add_task(
        send_email, new_user.email, new_user.username, request.base_url
    )
    return {"user": new_user, "detail": "User successfully created"}


@router.post("/login", response_model=TokenModel)
async def login(body: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)) -> dict | HTTPException:
    """
    The login function is used to authenticate a user.
        It takes in the username and password of the user, and returns an access token if successful.
        The access token can be used to make authenticated requests on behalf of that user.

    :param body: OAuth2PasswordRequestForm: Get the username and password from the request body
    :param db: Session: Get a database session
    :return: A dict with the access token and refresh token
    :rtype: dict | HTTPException
    """
    user = await repository_auth.get_user_by_email(body.username, db)
    # if not user.confirmed:
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Email not confirmed")
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email")
    if not auth_service.verify_password(body.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")

    # Generate JWT
    access_token = await auth_service.create_access_token(data={"sub": user.email})
    refresh_token = await auth_service.create_refresh_token(data={"sub": user.email})
    await repository_auth.update_token(user, refresh_token, db)
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


@router.get('/refresh_token', response_model=TokenModel)
async def refresh_token(credentials: HTTPAuthorizationCredentials = Security(security), db: Session = Depends(get_db)) -> dict | HTTPException:
    """
    The refresh_token function is used to refresh the access token.
        The function takes in a refresh token and returns an access token, a new refresh token, and the type of authentication being used.


    :param credentials: HTTPAuthorizationCredentials: Get the token from the request header
    :param db: Session: Pass the database session to the function
    :return: A dict with the new access token, refresh token and the bearer type
    :rtype: dict | HTTPException
    """
    token = credentials.credentials
    email = await auth_service.decode_refresh_token(token)
    user = await repository_auth.get_user_by_email(email, db)
    if user.refresh_token != token:
        await repository_auth.update_token(user, None, db)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

    access_token = await auth_service.create_access_token(data={"sub": email})
    refresh_token = await auth_service.create_refresh_token(data={"sub": email})
    await repository_auth.update_token(user, refresh_token, db)
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


@router.get('/confirmed_email/{token}')
async def confirmed_email(token: str, db: Session = Depends(get_db)) -> dict:
    """
    The confirmed_email function is used to confirm a user's email address.
        It takes in the token that was sent to the user's email and uses it to get their email address.
        Then, it gets the user from our database using their email address and checks if they exist.
        If they don't exist, we return an error message saying &quot;Verification error&quot;.
        If they do exist, we check if their account has already been confirmed or not.
        If it has been confirmed already, then we return a message saying &quot;Your email is already confirmed&quot;.

    :param token: str: Get the token from the url
    :param db: Session: Pass the database session to the function
    :return: A dictionary with a message
    :rtype: dict | HTTPException
    """
    email = await auth_service.get_email_from_token(token)
    user = await repository_auth.get_user_by_email(email, db)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Verification error")
    if user.confirmed:
        return {"message": "Your email is already confirmed"}
    await repository_auth.confirmed_email(email, db)
    return {"message": "Email confirmed"}


@router.post('/request_email')
async def request_email(body: RequestEmail, background_tasks: BackgroundTasks,
                        request: Request, db: Session = Depends(get_db)) -> dict:
    """
    The request_email function is used to send a confirmation email to the user.
        The function takes in an email address and sends a confirmation link to that address.
        If the user's account has already been confirmed, then they will be notified of this fact.

    :param body: RequestEmail: Get the email from the request body
    :param background_tasks: BackgroundTasks: Add a task to the background tasks queue
    :param request: Request: Get the base url of the server
    :param db: Session: Get the database session
    :return: A dictionary with a message
    :rtype: dict | HTTPException
    """
    user = await repository_auth.get_user_by_email(body.email, db)

    if user.confirmed:
        return {"message": "Your email is already confirmed"}
    if user:
        background_tasks.add_task(
            send_email, user.email, user.username, request.base_url)
    return {"message": "Check your email for confirmation."}

