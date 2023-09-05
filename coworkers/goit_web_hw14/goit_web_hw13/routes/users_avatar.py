from fastapi import APIRouter, Depends, status, UploadFile, File
from sqlalchemy.orm import Session

import cloudinary
import cloudinary.uploader

from goit_web_hw13.database.db import get_db
from goit_web_hw13.database.models import User
from goit_web_hw13.repository import auth as repository_auths
from goit_web_hw13.services.auth import auth_service
from goit_web_hw13.conf.config import settings
from goit_web_hw13.schemas import UserDb

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me/", response_model=UserDb)
async def read_users_me(
    current_user: User = Depends(auth_service.get_current_user),
) -> User:
    """
    The read and show information about curent user

    :param current_user: Get the current user
    :type current_user: User
    :return: The curent user
    :rtype: User
    """
    return current_user


@router.patch("/avatar", response_model=UserDb)
async def update_avatar_user(
    file: UploadFile = File(),
    current_user: User = Depends(auth_service.get_current_user),
    db: Session = Depends(get_db),
) -> User:
    """
    The update_avatar_user function updates the avatar of a user.

    :param file: UploadFile: Receive the file from the client
    :param current_user: User: Get the current user
    :param db: Session: Access the database
    :return: User: The updated user
    """
    cloudinary.config(
        cloud_name=settings.cloudinary_name,
        api_key=settings.cloudinary_api_key,
        api_secret=settings.cloudinary_api_secret,
        secure=True,
    )

    r = cloudinary.uploader.upload(
        file.file, public_id=f"NotesApp/{current_user.username}", overwrite=True
    )
    goit_web_hw13_url = cloudinary.CloudinaryImage(
        f"NotesApp/{current_user.username}"
    ).build_url(width=250, height=250, crop="fill", version=r.get("version"))
    user = await repository_auths.update_avatar(
        current_user.email, goit_web_hw13_url, db
    )
    return user
