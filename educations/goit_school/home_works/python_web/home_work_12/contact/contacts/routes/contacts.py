from typing import Annotated
from pydantic import EmailStr
from fastapi import APIRouter, Depends, HTTPException, Path, status, Query
from sqlalchemy.orm import Session

from contacts.database.db import get_db
from contacts.database.models import User
from contacts.schemas import ContactResponse, ContactModel
from contacts.repository import contacts as repository_contacts
from contacts.services.auth import auth_service

router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.get("/", response_model=list[ContactResponse])
async def get_contacts(limit: int = Query(5, le=300), offset: int = 0,
                       db: Session = Depends(get_db),
                       user: User = Depends(auth_service.get_current_user)):
    contacts = await repository_contacts.get_contacts(limit, offset, db, user)
    return contacts


@router.get("/{contact_id}", response_model=ContactResponse)
async def get_contact_by_id(contact_id: int = Path(ge=1),
                            db: Session = Depends(get_db),
                            user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contacts.get_contact_by_id(contact_id, db, user)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return contact


@router.get("/search_contacts/", response_model=list[ContactResponse])
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
                              ):
    contacts = await repository_contacts.get_search_contacts(limit, offset, db, user, contact_first_name,
                                                             contact_last_name)
    return contacts


@router.get("/contacts_by_email/", response_model=ContactResponse)
async def get_contacts_by_email(contact_email: EmailStr,
                                db: Session = Depends(get_db),
                                user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contacts.get_contacts_by_email(contact_email, db, user)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return contact


@router.post("/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_contact(body: ContactModel, db: Session = Depends(get_db),
                         user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contacts.create_contact(body, db, user)
    return contact


@router.put("/{contact_id}", response_model=ContactResponse)
async def update_contact(body: ContactModel, contact_id: int = Path(ge=1),
                         db: Session = Depends(get_db),
                         user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contacts.update_contact(contact_id, body, db, user)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return contact


@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(contact_id: int = Path(ge=1),
                         db: Session = Depends(get_db),
                         user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contacts.delete_contact(contact_id, db, user)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return None


@router.get("/birthday_next_days/",
            response_model=list[ContactResponse])
async def get_contacts_by_birthday(limit: int = Query(10, le=300),
                                   offset: int = 0,
                                   db: Session = Depends(get_db),
                                   user: User = Depends(auth_service.get_current_user)):
    contacts = await repository_contacts.get_contacts_by_birthday(limit, offset, db, user)
    return contacts
