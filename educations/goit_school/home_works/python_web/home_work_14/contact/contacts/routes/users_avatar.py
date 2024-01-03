from fastapi import APIRouter, Depends, status, UploadFile, File
from sqlalchemy.orm import Session

import cloudinary
import cloudinary.uploader

from contacts.database.db import get_db
from contacts.database.models import User
from contacts.repository import auth as repository_auths
from contacts.services.auth import auth_service
from contacts.conf.config import settings
from contacts.schemas import UserDb

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me/", response_model=UserDb)
async def read_users_me(current_user: User = Depends(auth_service.get_current_user)) -> User:
    """
    The read_users_me function returns the current user's information.

    :param current_user: User: Get the current user
    :return: The current user
    :rtype: User
    """
    return current_user


@router.patch('/avatar', response_model=UserDb)
async def update_avatar_user(file: UploadFile = File(),
                             current_user: User = Depends(
                                 auth_service.get_current_user),
                             db: Session = Depends(get_db)) -> User:
    """
    The update_avatar_user function is used to update the avatar of a user.
        The function takes in an UploadFile object, which is a file that has been uploaded by the client.
        It also takes in the current_user and db objects as dependencies.

    :param file: UploadFile: Upload the file to cloudinary
    :param current_user: User: Get the current user
    :param db: Session: Get the database session
    :return: The updated user object
    :rtype: User
    """
    cloudinary.config(
        cloud_name=settings.cloudinary_name,
        api_key=settings.cloudinary_api_key,
        api_secret=settings.cloudinary_api_secret,
        secure=True
    )

    r = cloudinary.uploader.upload(
        file.file, public_id=f'NotesApp/{current_user.username}', overwrite=True)
    url = cloudinary.CloudinaryImage(f'NotesApp/{current_user.username}')\
                        .build_url(width=250, height=250, crop='fill', version=r.get('version'))
    user = await repository_auths.update_avatar(current_user.email, url, db)
    return user
