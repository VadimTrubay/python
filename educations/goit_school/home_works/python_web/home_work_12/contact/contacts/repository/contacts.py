from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from sqlalchemy import and_

from contacts.database.models import Contact, User
from contacts.schemas import ContactModel


async def get_contacts(limit: int, offset: int, db: Session, user: User):
    contacts = db.query(Contact).filter_by(user_id=user.id).limit(limit).offset(offset)
    return contacts.all()


async def get_contact_by_id(contact_id: int, db: Session, user: User):
    contact = db.query(Contact).filter(and_(Contact.user_id == user.id, Contact.id == contact_id)).first()
    return contact


async def get_search_contacts(limit: int, offset: int,
                              db: Session,
                              user: User,
                              contact_first_name: str | None = None,
                              contact_last_name: str | None = None
                              ):
    contacts = db.query(Contact).filter_by(user_id=user.id)
    if contact_first_name:
        contacts = contacts.filter_by(contact_first_name=contact_first_name)
    if contact_last_name:
        contacts = contacts.filter_by(contact_last_name=contact_last_name)
    return contacts.limit(limit).offset(offset).all()


async def get_contact_by_email(user_email: str, db: Session, user: User):
    contact = db.query(Contact).filter(and_(Contact.user_id == user.id, Contact.email == user_email)).first()
    return contact


async def create_contact(body: ContactModel, db: Session, user: User):
    contact = Contact(**body.dict())
    contact.user_id = user.id
    db.add(contact)
    db.commit()
    return contact


async def update_contact(contact_id: int, body: ContactModel, db: Session, user: User):
    contact = await get_contact_by_id(contact_id, db, user)
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.phone = body.phone
        contact.birthday = body.birthday
        contact.user_id = user.id
        contact.information = body.information
        db.commit()
    return contact


async def delete_contact(user_id: int, db: Session, user: User):
    contact = await get_contacts_by_id(user_id, db, user)
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def get_contacts_by_birthday(limit: int, offset: int, db: Session, user: User):
    current_datetime = datetime.now().date()
    date_end_birthdays = current_datetime + timedelta(days=7)
    contacts = db.query(Contact).filter_by(user_id=user.id).limit(limit).offset(offset).all()
    contacts_birthdays = []
    for contact in contacts:
        contact_birthday = contact.birthday
        birthday_this_year = datetime(
            current_datetime.year,
            contact_birthday.month,
            contact_birthday.day
        ).date()
        if current_datetime < birthday_this_year < date_end_birthdays:
            contacts_birthdays.append(contact)
    return contacts_birthdays
