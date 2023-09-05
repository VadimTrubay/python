from typing import Annotated
from pydantic import EmailStr
from fastapi import APIRouter, Depends, HTTPException, Path, status, Query
from fastapi_limiter.depends import RateLimiter
from sqlalchemy.orm import Session

from goit_web_hw13.database.db import get_db
from goit_web_hw13.database.models import User, UserContact
from goit_web_hw13.schemas import ContactResponse, ContactModel
from goit_web_hw13.repository import contacts as repository_contacts
from goit_web_hw13.services.auth import auth_service

router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.get(
    "/",
    response_model=list[ContactResponse],
    description="No more than 2 requests per 10 seconds and 10 requests per minute",
    dependencies=[
        Depends(RateLimiter(times=2, seconds=10)),
        Depends(RateLimiter(times=10, seconds=60)),
    ],
)
async def get_contacts(
    limit: int = Query(10, le=300),
    offset: int = 0,
    db: Session = Depends(get_db),
    user: User = Depends(auth_service.get_current_user),
) -> list[UserContact]:
    """
    Retrieves a list of contacts for a specific user with
    specified pagination parameters. Limit on the number of requests

    :param limit: The maximum number of contacts to return.
    :type limit: int
    :param offset: The number of contacts to skip.
    :type offset: int
    :param db: The database session.
    :type db: Session
    :param user: The user to retrieve contacts for.
    :type user: User
    :return: A list of contacts.
    :rtype: list[UserContact]
    """
    contacts = await repository_contacts.get_contacts(limit, offset, db, user)
    return contacts


@router.get(
    "/{contact_id}",
    response_model=ContactResponse,
    description="No more than 2 requests per 10 seconds and 10 requests per minute",
    dependencies=[
        Depends(RateLimiter(times=2, seconds=10)),
        Depends(RateLimiter(times=10, seconds=60)),
    ],
)
async def get_contact(
    contact_id: int = Path(ge=1),
    db: Session = Depends(get_db),
    user: User = Depends(auth_service.get_current_user),
) -> UserContact | None:
    """
    Retrieves a single contact with the specified ID for a specific user.
    Limit on the number of requests

    :param contact_id: The ID of the contact to retrieve.
    :type contact_id: int
    :param user: The user to retrieve the contact for.
    :type user: User
    :param db: The database session.
    :type db: Session
    :return: The contact with the specified ID, or HTTPException if it does not exist.
    :rtype: UserContact | None
    """
    contact = await repository_contacts.get_contact_by_id(contact_id, db, user)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return contact


@router.get(
    "/search_contacts/",
    response_model=list[ContactResponse],
    description="No more than 2 requests per 10 seconds and 10 requests per minute",
    dependencies=[
        Depends(RateLimiter(times=2, seconds=10)),
        Depends(RateLimiter(times=10, seconds=60)),
    ],
)
async def search_contacts(
    limit: Annotated[int, Query(le=50)] = 10,
    offset: int = 0,
    db: Session = Depends(get_db),
    user: User = Depends(auth_service.get_current_user),
    contact_name: Annotated[
        str | None,
        Query(
            description="""_may be empty_ 
                                                 **---to get all users, the following fields must be empty---**""",
            max_length=20,
        ),
    ] = None,
    contact_surname: Annotated[
        str | None, Query(description="may be empty", max_length=30)
    ] = None,
) -> list[UserContact]:
    """
    Retrieves a list of contacts with a given name and/or surname
    for a specific user with specified pagination parameters.
    Limit on the number of requests

    :param limit: The maximum number of contacts to return.
    :type limit: int
    :param offset: The number of contacts to skip.
    :type offset: int
    :param db: The database session.
    :type db: Session
    :param user: The user to retrieve contacts for.
    :type user: User
    :param contact_name: contact name
    :type contact_name: str | None
    :param contact_surname: contact surname
    :type contact_surname: str | None
    :return: A list of contacts.
    :rtype: list[UserContact]
    """
    contacts = await repository_contacts.get_search_contacts(
        limit, offset, db, user, contact_name, contact_surname
    )
    return contacts


@router.get(
    "/contacts_by_email/",
    response_model=ContactResponse,
    description="No more than 2 requests per 10 seconds and 10 requests per minute",
    dependencies=[
        Depends(RateLimiter(times=2, seconds=10)),
        Depends(RateLimiter(times=10, seconds=60)),
    ],
)
async def get_contacts_by_email(
    contact_email: EmailStr,
    db: Session = Depends(get_db),
    user: User = Depends(auth_service.get_current_user),
) -> UserContact | None:
    """
    Retrieves a single contact with a given email for a specific user.
    Limit on the number of requests

    :param contact_email: The email of the contact to retrieve.
    :type contact_email: str
    :param db: The database session.
    :type db: Session
    :param user: The user to retrieve the contact for.
    :type user: User
    :return: The contact with a given email
    :rtype: User
    """
    contact = await repository_contacts.get_contacts_by_email(contact_email, db, user)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return contact


@router.post(
    "/",
    response_model=ContactResponse,
    description="No more than 10 contacts per minute",
    dependencies=[Depends(RateLimiter(times=10, seconds=60))],
    status_code=status.HTTP_201_CREATED,
)
async def create_contact(
    body: ContactModel,
    db: Session = Depends(get_db),
    user: User = Depends(auth_service.get_current_user),
) -> UserContact:
    """
    Creates a new contact for a specific user.
    Limit on the number of creates

    :param body: The data for the contact to create.
    :type body: ContactModel
    :param db: The database session.
    :type db: Session
    :param user: The user to create the contact for.
    :type user: User
    :return: The newly created contact.
    :rtype: UserContact
    """
    contact = await repository_contacts.create(body, db, user)
    return contact


@router.put(
    "/{contact_id}",
    response_model=ContactResponse,
    description="No more 10 requests per minute",
    dependencies=[Depends(RateLimiter(times=10, seconds=60))],
)
async def update_contact(
    body: ContactModel,
    contact_id: int = Path(ge=1),
    db: Session = Depends(get_db),
    user: User = Depends(auth_service.get_current_user),
) -> UserContact:
    """
    Updates a single contact with the specified ID for a specific
    user. Limit on the number of updates

    :param id: The ID of the contact to update.
    :type id: int
    :param body: The updated data for the contact.
    :type body: ContactModel
    :param user: The user to update the contact for.
    :type user: User
    :param db: The database session.
    :type db: Session
    :return: The updated contact, or HTTPException if it does not exist.
    :rtype: UserContact | None
    """
    contact = await repository_contacts.update(contact_id, body, db, user)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return contact


@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(
    contact_id: int = Path(ge=1),
    db: Session = Depends(get_db),
    user: User = Depends(auth_service.get_current_user),
) -> None:
    """
    Removes a single contact with the specified ID for a specific user.

    :param id: The ID of the contact to remove.
    :type id: int
    :param user: The user to remove the contact for.
    :type user: User
    :param db: The database session.
    :type db: Session
    :return: The removed None, or HTTPException if it does not exist.
    :rtype: None | HTTPException
    """
    contact = await repository_contacts.remove(contact_id, db, user)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return None


@router.get(
    "/bithday_next_days/",
    response_model=list[ContactResponse],
    description="No more than 2 requests per 10 seconds and 10 requests per minute",
    dependencies=[
        Depends(RateLimiter(times=2, seconds=10)),
        Depends(RateLimiter(times=10, seconds=60)),
    ],
)
async def get_contacts_by_bithday(
    limit: int = Query(10, le=300),
    offset: int = 0,
    db: Session = Depends(get_db),
    user: User = Depends(auth_service.get_current_user),
) -> list[UserContact]:
    """
    Retrieves a list of contacts, who have a birthday in the next few days,
    the number of which is specified in the constant NEXT_DAYS(= 7)
    for a specific user with specified pagination parameters.
    Limit on the number of requests

    :param limit: The maximum number of contacts to return.
    :type limit: int
    :param offset: The number of contacts to skip.
    :type offset: int
    :param db: The database session.
    :type db: Session
    :param user: The user to retrieve contacts for.
    :type user: User
    :return: A list of contacts.
    :rtype: list[UserContact]
    """
    contacts = await repository_contacts.get_contacts_by_bithday(
        limit, offset, db, user
    )
    return contacts
