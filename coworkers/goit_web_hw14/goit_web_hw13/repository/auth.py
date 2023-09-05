import logging

from libgravatar import Gravatar
from sqlalchemy.orm import Session

from goit_web_hw13.database.models import User
from goit_web_hw13.schemas import UserModel


async def get_user_by_email(email: str, db: Session) -> User | None:
    """
    Receives a user by their email address.

    :param email: The email of the user you want to find.
    :type email: str
    :param db: The database session.
    :type db: Session
    :return: The user with a given email, or None if it does not exist.
    :rtype: User | None
    """
    return db.query(User).filter(User.email == email).first()


async def create_user(body: UserModel, db: Session) -> User:
    """
    Creates a new user.

    :param body: The data for the user to create.
    :type body: UserModel
    :param db: The database session.
    :type db: Session
    :return: The newly created user.
    :rtype: User
    """
    avatar = None
    try:
        g = Gravatar(body.email)
        avatar = g.get_image()
    except Exception as e:
        logging.error(e)

    new_user = User(**body.dict(), avatar=avatar)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def update_token(user: User, token: str | None, db: Session) -> None:
    """
    updates refresh_token in the database

    :param user: The user to update the token
    :type user: User
    :param token: token that is added to the database
    :type token: str|None
    :param db: The database session.
    :type db: Session
    :return: None
    """
    user.refresh_token = token
    db.commit()


async def confirmed_email(email: str, db: Session) -> None:
    """
    Sets the email confirmation flag to True

    :param email: The email of the user.
    :type email: str
    :param db: The database session.
    :type db: Session
    :return: None
    """
    user = await get_user_by_email(email, db)
    user.confirmed = True
    db.commit()


async def update_avatar(email: str, url: str, db: Session) -> User:
    """
    updates avatar in the database

    :param email: The email of the user.
    :type email: str
    :param url: The path to the avatar.
    :type url: str
    :param db: The database session.
    :type db: Session
    :return: The user with avatar.
    :rtype: User
    """
    user = await get_user_by_email(email, db)
    user.avatar = url
    db.commit()
    return user
