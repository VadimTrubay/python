from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from contacts.database.models import Contact
from contacts.schemas import ContactModel


async def get_contacts(limit: int, offset: int, db: Session):
    contacts = db.query(Contact).limit(limit).offset(offset)
    return contacts.all()


async def get_contact_by_id(contact_id: int, db: Session):
    contact = db.query(Contact).filter_by(id=contact_id).first()
    return contact


async def get_search_contacts(limit: int, offset: int,
                              db: Session,
                              contact_first_name: str | None = None,
                              contact_last_name: str | None = None
                              ):
    contacts = db.query(Contact)
    if contact_first_name:
        contacts = contacts.filter_by(first_name=contact_first_name)
    if contact_last_name:
        contacts = contacts.filter_by(last_name=contact_last_name)
    return contacts.limit(limit).offset(offset).all()


async def get_contacts_by_birthday(limit: int, offset: int, db: Session):
    current_datetime = datetime.now().date()
    date_end_birthdays = current_datetime + timedelta(days=7)
    contacts = db.query(Contact).all()
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


async def get_contacts_by_email(contact_email: str, db: Session):
    contact = db.query(Contact).filter_by(email=contact_email).first()
    return contact


async def create(body: ContactModel, db: Session):
    contact = Contact(**body.dict())
    print(contact)
    db.add(contact)
    db.commit()
    return contact


async def update(contact_id: int, body: ContactModel, db: Session):
    contact = await get_contact_by_id(contact_id, db)
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.phone = body.phone
        contact.birthday = body.birthday
        contact.information = body.information
        db.commit()
    return contact


async def remove(contact_id: int, db: Session):
    contact = await get_contact_by_id(contact_id, db)
    if contact:
        db.delete(contact)
        db.commit()
    return contact
