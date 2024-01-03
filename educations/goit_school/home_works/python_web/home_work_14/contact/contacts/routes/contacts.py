from typing import Annotated
from pydantic import EmailStr
from fastapi import APIRouter, Depends, HTTPException, Path, status, Query
from sqlalchemy.orm import Session
from fastapi_limiter.depends import RateLimiter

from contacts.database.db import get_db
from contacts.database.models import User, Contact
from contacts.schemas import ContactResponse, ContactModel
from contacts.repository import contacts as repository_contacts
from contacts.services.auth import auth_service

router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.get("/", response_model=list[ContactResponse],
            description='No more than 2 requests per 10 seconds and 10 requests per minute',
            dependencies=[
                Depends(RateLimiter(times=2, seconds=10)),
                Depends(RateLimiter(times=10, seconds=60))
            ]
            )
async def get_contacts(limit: int = Query(5, le=300), offset: int = 0,
                       db: Session = Depends(get_db),
                       user: User = Depends(auth_service.get_current_user)) -> list[Contact]:
    """
    The get_contacts function returns a list of contacts for the current user.

    :param limit: int: Limit the number of contacts returned
    :param le: Limit the number of contacts returned
    :param offset: int: Skip the first offset contacts
    :param db: Session: Get the database session
    :param user: Contact : Get the current user
    :return: A list of contacts
    :rtype: list[Contact ]
    """
    contacts = await repository_contacts.get_contacts(limit, offset, db, user)
    return contacts


@router.get("/{contact_id}", response_model=ContactResponse,
            description='No more than 2 requests per 10 seconds and 10 requests per minute',
            dependencies=[
                Depends(RateLimiter(times=2, seconds=10)),
                Depends(RateLimiter(times=10, seconds=60))
                ]
            )
async def get_contact_by_id(contact_id: int = Path(ge=1),
                            db: Session = Depends(get_db),
                            user: User = Depends(auth_service.get_current_user)) -> Contact | None:
    """
    The get_contact_by_id function returns a contact by its id.

    :param contact_id: int: Specify the contact id that will be used to retrieve a specific contact
    :param db: Session: Get the database session
    :param user: User: Get the current user from the auth_service
    :return: A contact object or none
    :rtype: Contact | None
    """
    contact = await repository_contacts.get_contact_by_id(contact_id, db, user)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return contact


@router.get("/search_contacts/", response_model=list[ContactResponse],
            description='No more than 2 requests per 10 seconds and 10 requests per minute',
            dependencies=[
                Depends(RateLimiter(times=2, seconds=10)),
                Depends(RateLimiter(times=10, seconds=60))
                ]
            )
async def get_search_contacts(limit: Annotated[int, Query(le=50)] = 10,
                              offset: int = 0,
                              db: Session = Depends(get_db),
                              user: User = Depends(auth_service.get_current_user),
                              contact_first_name: Annotated[str | None,
                                                            Query(description="enter contact_first_name",
                                                                  max_length=20)] = None,
                              contact_last_name: Annotated[str | None,
                                                           Query(description="enter contact_last_name",
                                                                 max_length=30)] = None
                              ) -> list[Contact]:
    """
    The get_search_contacts function is used to search for contacts in the database.
        The user can enter a contact_first_name and/or a contact_last_name, which will be searched for in the database.
        If no name is entered, all contacts are returned.

    :param limit: The maximum number of contacts to return.
    :type limit: int
    :param offset: The number of contacts to skip.
    :type offset: int
    :param db: The database session.
    :type db: Session
    :param user: The user to retrieve contacts for.
    :type user: User
    :param contact_first_name: contact name
    :type contact_first_name: str | None
    :param contact_last_name: contact surname
    :type contact_last_name: str | None
    :return: A list of contacts.
    :rtype: list[Contact]
    """
    contacts = await repository_contacts.get_search_contacts(limit, offset, db, user, contact_first_name,
                                                             contact_last_name)
    return contacts


@router.get("/contacts_by_email/", response_model=ContactResponse,
            description='No more than 2 requests per 10 seconds and 10 requests per minute',
            dependencies=[
                Depends(RateLimiter(times=2, seconds=10)),
                Depends(RateLimiter(times=10, seconds=60))
                ]
            )
async def get_contacts_by_email(contact_email: EmailStr,
                                db: Session = Depends(get_db),
                                user: User = Depends(auth_service.get_current_user)) -> Contact | None:
    """
    The get_contacts_by_email function returns a contact by email.

    :param contact_email: EmailStr: Get the contact email from the request body
    :param db: Session: Pass the database session to the function
    :param user: User: Get the current user from the auth_service
    :return: A contact object or none if the contact is not found
    :rtype: Contact | None
    """
    contact = await repository_contacts.get_contacts_by_email(contact_email, db, user)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return contact


@router.post("/", response_model=ContactResponse,
             description='No more than 10 contacts per minute',
             dependencies=[Depends(RateLimiter(times=10, seconds=60))],
             status_code=status.HTTP_201_CREATED)
async def create_contact(body: ContactModel, db: Session = Depends(get_db),
                         user: User = Depends(auth_service.get_current_user)) -> Contact:
    """
    The create_contact function creates a new contact in the database.

    :param body: ContactModel: Get the data from the request body
    :param db: Session: Get the database session
    :param user: User: Get the current user from the auth_service
    :return: A contact object
    :rtype: Contact
    """
    contact = await repository_contacts.create_contact(body, db, user)
    return contact


@router.put("/{contact_id}", response_model=ContactResponse,
            description='No more 10 requests per minute',
            dependencies=[Depends(RateLimiter(times=10, seconds=60))]
            )
async def update_contact(body: ContactModel, contact_id: int = Path(ge=1),
                         db: Session = Depends(get_db),
                         user: User = Depends(auth_service.get_current_user)) -> Contact:
    """
    The update_contact function updates a contact in the database.
        The function takes an id, body and db as parameters.
        It returns a Contact object.

    :param body: ContactModel: Get the data from the request body
    :param contact_id: int: Specify the contact_id of the contact to be deleted
    :param db: Session: Get the database session
    :param user: User: Get the current user
    :return: A contact object
    :rtype: Contact | None
    """
    contact = await repository_contacts.update_contact(contact_id, body, db, user)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return contact


@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(contact_id: int = Path(ge=1),
                         db: Session = Depends(get_db),
                         user: User = Depends(auth_service.get_current_user)) -> None:
    """
    The delete_contact function deletes a contact from the database.
        The function takes in an integer representing the id of the contact to be deleted,
        and returns None if successful.

    :param contact_id: int: Specify the contact id of the contact to be deleted
    :param db: Session: Pass the database session to the function
    :param user: User: Get the current user
    :return: The removed None, or HTTPException if it does not exist.
    :rtype: None | HTTPException
    """
    contact = await repository_contacts.delete_contact(contact_id, db, user)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return None


@router.get("/birthday_next_days/",
            response_model=list[ContactResponse],
            description='No more than 2 requests per 10 seconds and 10 requests per minute',
            dependencies=[
                Depends(RateLimiter(times=2, seconds=10)),
                Depends(RateLimiter(times=10, seconds=60))
                ]
            )
async def get_contacts_by_birthday(limit: int = Query(10, le=300),
                                   offset: int = 0,
                                   db: Session = Depends(get_db),
                                   user: User = Depends(auth_service.get_current_user)) -> list[Contact]:
    """
    The get_contacts_by_birthday function returns a list of contacts sorted by birthday.

    :param limit: int: Limit the number of contacts returned
    :param le: Limit the maximum number of contacts returned
    :param offset: int: Specify the number of records to skip
    :param db: Session: Pass the database session to the repository
    :param user: User: Get the current user from the auth_service
    :return: A list of contacts
    :rtype: list[Contact]
    """
    contacts = await repository_contacts.get_contacts_by_birthday(limit, offset, db, user)
    return contacts
