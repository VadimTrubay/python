import logging

from libgravatar import Gravatar
from sqlalchemy.orm import Session

from contacts.database.models import User
from contacts.schemas import UserModel


async def get_user_by_email(email: str, db: Session) -> User | None:
    """
    The get_user_by_email function takes in an email and a database session,
    and returns the user associated with that email. If no such user exists, it returns None.

    :param email: str: Specify the email of the user we want to retrieve
    :param db: Session: Connect to the database
    :return: The first user in the database with the specified email address
    :rtype: User | None
    """
    return db.query(User).filter(User.email == email).first()


async def create_user(body: UserModel, db: Session) -> User:

    """
    The create_user function creates a new user in the database.

    :param body: UserModel: Get the user data from the request body
    :param db: Session: Access the database
    :return: A user object
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
    The update_token function updates the refresh token for a user in the database.

    :param user: User: Pass in the user object that is being updated
    :param token: str | None: Update the user's refresh token in the database
    :param db: Session: Access the database
    :return: None
    """
    user.refresh_token = token
    db.commit()


async def confirmed_email(email: str, db: Session) -> None:
    """
    The confirmed_email function takes in an email and a database session,
    and sets the confirmed field of the user with that email to True.


    :param email: str: Pass in the email of the user that is being confirmed
    :param db: Session: Pass in the database session
    :return: None
    """
    user = await get_user_by_email(email, db)
    user.confirmed = True
    db.commit()


async def update_avatar(email, url: str, db: Session) -> User:
    """
    The update_avatar function updates the avatar of a user in the database.
        Args:
            email (str): The email of the user to update.
            url (str): The new URL for their avatar image.

    :param email: Find the user in the database
    :param url: str: Pass in the url of the avatar image
    :param db: Session: Access the database
    :return: The user object with the updated avatar url
    :rtype: User
    """
    user = await get_user_by_email(email, db)
    user.avatar = url
    print(user.avatar)
    db.commit()
    return user