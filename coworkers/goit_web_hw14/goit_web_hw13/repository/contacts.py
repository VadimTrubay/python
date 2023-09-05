from sqlalchemy import and_
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from goit_web_hw13.database.models import UserContact, User
from goit_web_hw13.schemas import ContactModel

NEXT_DAYS = 7


async def get_contacts(
    limit: int, offset: int, db: Session, user: User
) -> list[UserContact]:
    """
    Retrieves a list of contacts for a specific user with specified pagination parameters.

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
    contacts = (
        db.query(UserContact).filter_by(user_id=user.id).limit(limit).offset(offset)
    )
    return contacts.all()


async def get_contact_by_id(
    contact_id: int, db: Session, user: User
) -> UserContact | None:
    """
    Retrieves a single contact with the specified ID for a specific user.

    :param contact_id: The ID of the contact to retrieve.
    :type contact_id: int
    :param user: The user to retrieve the contact for.
    :type user: User
    :param db: The database session.
    :type db: Session
    :return: The contact with the specified ID, or None if it does not exist.
    :rtype: UserContact | None
    """
    contact = (
        db.query(UserContact)
        .filter(and_(UserContact.user_id == user.id, UserContact.id == contact_id))
        .first()
    )
    return contact


async def get_search_contacts(
    limit: int,
    offset: int,
    db: Session,
    user: User,
    contact_name: str | None = None,
    contact_surname: str | None = None,
) -> list[UserContact]:
    """
    Retrieves a list of contacts with a given name and/or surname
    for a specific user with specified pagination parameters.

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
    contacts = db.query(UserContact).filter_by(user_id=user.id)
    if contact_name:
        contacts = contacts.filter_by(name=contact_name)
    if contact_surname:
        contacts = contacts.filter_by(surname=contact_surname)
    return contacts.limit(limit).offset(offset).all()


async def get_contacts_by_bithday(
    limit: int, offset: int, db: Session, user: User
) -> list[UserContact]:
    """
    Retrieves a list of contacts, who have a birthday in the next few days,
    the number of which is specified in the constant NEXT_DAYS(= 7)
    for a specific user with specified pagination parameters.

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
    current_datetime = datetime.now().date()
    date_end_bithdays = current_datetime + timedelta(days=NEXT_DAYS)
    contacts = (
        db.query(UserContact)
        .filter_by(user_id=user.id)
        .limit(limit)
        .offset(offset)
        .all()
    )
    contacts_bithdays = []
    for contact in contacts:
        contact_bithday = contact.bithday
        bithday_this_year = datetime(
            current_datetime.year, contact_bithday.month, contact_bithday.day
        ).date()
        if current_datetime <= bithday_this_year < date_end_bithdays:
            contacts_bithdays.append(contact)
    return contacts_bithdays


async def get_contacts_by_email(
    contact_email: str, db: Session, user: User
) -> UserContact | None:
    """
    Retrieves a single contact with a given email for a specific user.

    :param contact_email: The email of the contact to retrieve.
    :type contact_email: str
    :param db: The database session.
    :type db: Session
    :param user: The user to retrieve the contact for.
    :type user: User
    :return: The contact with a given email, or None if it does not exist.
    :rtype: UserContact | None
    """
    contact = (
        db.query(UserContact)
        .filter(
            and_(UserContact.user_id == user.id, UserContact.email == contact_email)
        )
        .first()
    )
    return contact


async def create(body: ContactModel, db: Session, user: User) -> UserContact:
    """
    Creates a new contact for a specific user.

    :param body: The data for the contact to create.
    :type body: ContactModel
    :param db: The database session.
    :type db: Session
    :param user: The user to create the contact for.
    :type user: User
    :return: The newly created contact.
    :rtype: UserContact
    """
    contact = UserContact(**body.dict())
    contact.user_id = user.id
    db.add(contact)
    db.commit()
    return contact


async def update(id: int, body: ContactModel, db: Session, user: User) -> UserContact:
    """
    Updates a single contact with the specified ID for a specific user.

    :param id: The ID of the contact to update.
    :type id: int
    :param body: The updated data for the contact.
    :type body: ContactModel
    :param user: The user to update the contact for.
    :type user: User
    :param db: The database session.
    :type db: Session
    :return: The updated contact, or None if it does not exist.
    :rtype: UserContact | None
    """
    contact = await get_contact_by_id(id, db, user)
    if contact:
        contact.name = body.name
        contact.surname = body.surname
        contact.email = body.email
        contact.phone = body.phone
        contact.bithday = body.bithday
        contact.user_id = user.id
        contact.information = body.information
        db.commit()
    return contact


async def remove(id: int, db: Session, user: User) -> UserContact | None:
    """
    Removes a single contact with the specified ID for a specific user.

    :param id: The ID of the contact to remove.
    :type id: int
    :param user: The user to remove the contact for.
    :type user: User
    :param db: The database session.
    :type db: Session
    :return: The removed contact, or None if it does not exist.
    :rtype: UserContact | None
    """
    contact = await get_contact_by_id(id, db, user)
    if contact:
        db.delete(contact)
        db.commit()
    return contact
