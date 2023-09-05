from typing import Annotated
from pydantic import EmailStr
from fastapi import APIRouter, Depends, HTTPException, Path, status, Query
from fastapi_limiter.depends import RateLimiter
from sqlalchemy.orm import Session

from goit_web_hw13.database.db import get_db
from goit_web_hw13.database.models import User
from goit_web_hw13.schemas import ContactResponse, ContactModel
from goit_web_hw13.repository import contacts as repository_contacts
from goit_web_hw13.services.auth import auth_service

router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.get("/", response_model=list[ContactResponse],
            description='No more than 2 requests per 10 seconds and 10 requests per minute',
            dependencies=[
                Depends(RateLimiter(times=2, seconds=10)),
                Depends(RateLimiter(times=10, seconds=60))
                ]
            )
async def get_contacts(limit: int = Query(10, le=300), offset: int = 0, 
                    db: Session = Depends(get_db), 
                    user: User = Depends(auth_service.get_current_user)):
    contacts = await repository_contacts.get_contacts(limit, offset, db, user)
    return contacts


@router.get("/{contact_id}", response_model=ContactResponse,
            description='No more than 2 requests per 10 seconds and 10 requests per minute',
            dependencies=[
                Depends(RateLimiter(times=2, seconds=10)),
                Depends(RateLimiter(times=10, seconds=60))
                ]
            )
async def get_contact(contact_id: int = Path(ge=1),
                   db: Session = Depends(get_db),
                   user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contacts.get_contact_by_id(contact_id, db, user)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Not found!")
    return contact


@router.get("/search_contacts/", response_model=list[ContactResponse],
            description='No more than 2 requests per 10 seconds and 10 requests per minute',
            dependencies=[
                Depends(RateLimiter(times=2, seconds=10)),
                Depends(RateLimiter(times=10, seconds=60))
                ]
            )
async def search_contacts(limit: Annotated[int, Query(le=50)] = 10, 
                            offset: int = 0, 
                            db: Session = Depends(get_db),
                            user: User = Depends(auth_service.get_current_user),
                            contact_name: Annotated[str | None, 
                                                 Query(description="""_may be empty_ 
                                                 **---to get all users, the following fields must be empty---**""", 
                                                       max_length=20)] = None, 
                            contact_surname: Annotated[str | None,
                                                    Query(description='may be empty', 
                                                          max_length=30)] = None                            
                            ):
    contacts = await repository_contacts.get_search_contacts(limit,
                                                     offset, 
                                                     db, user,
                                                    contact_name,
                                                    contact_surname
                                                     )
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
                            user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contacts.get_contacts_by_email(contact_email, db, user)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Not found!")
    return contact


@router.post("/", response_model=ContactResponse, 
             description='No more than 10 contacts per minute',
             dependencies=[Depends(RateLimiter(times=10, seconds=60))],
             status_code=status.HTTP_201_CREATED)
async def create_contact(body: ContactModel, db: Session = Depends(get_db),
                      user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contacts.create(body, db, user)
    return contact


@router.put("/{contact_id}", response_model=ContactResponse,
            description='No more 10 requests per minute',
            dependencies=[Depends(RateLimiter(times=10, seconds=60))]
            )
async def update_contact(body: ContactModel, contact_id: int = Path(ge=1),
                      db: Session = Depends(get_db),
                      user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contacts.update(contact_id, body, db, user)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Not found!")
    return contact


@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(contact_id: int = Path(ge=1),
                      db: Session = Depends(get_db),
                      user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contacts.remove(contact_id, db, user)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Not found!")
    return None


@router.get("/bithday_next_days/", 
            response_model=list[ContactResponse],
            description='No more than 2 requests per 10 seconds and 10 requests per minute',
            dependencies=[
                Depends(RateLimiter(times=2, seconds=10)),
                Depends(RateLimiter(times=10, seconds=60))
                ]
            )
async def get_contacts_by_bithday(limit: int = Query(10, le=300), 
                               offset: int = 0, 
                               db: Session = Depends(get_db),
                               user: User = Depends(auth_service.get_current_user)):
    contacts = await repository_contacts.get_contacts_by_bithday(limit,
                                                        offset, 
                                                        db, user)
    return contacts
