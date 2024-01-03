from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from sqlalchemy import and_

from contacts.database.models import Contact, User
from contacts.schemas import ContactModel


async def get_contacts(limit: int, offset: int, db: Session, user: User) -> list[Contact]:
    """
    The get_contacts function returns a list of contacts for the user.

    :param limit: int: Limit the number of contacts returned
    :param offset: int: Specify the starting point for the query
    :param db: Session: Access the database
    :param user: User: Get the user_id from the database
    :return: A list of contacts
    :rtype: list[Contact]
    """
    contacts = db.query(Contact).filter_by(user_id=user.id).limit(limit).offset(offset)
    return contacts.all()


async def get_contact_by_id(contact_id: int, db: Session, user: User) -> Contact | None:
    """
    The get_contact_by_id function takes in a contact_id and returns the corresponding Contact object.
        Args:
            contact_id (int): The id of the desired Contact object.
            db (Session): A database session to query for the desired Contact object.
            user (User): The current user, used to ensure that only contacts belonging to this user are returned.

    :param contact_id: int: Specify the id of the contact that you want to retrieve
    :param db: Session: Access the database
    :param user: User: Check if the user is logged in
    :return: A contact object
    :rtype: Contact | None
    """
    contact = db.query(Contact).filter(and_(Contact.user_id == user.id, Contact.id == contact_id)).first()
    return contact


async def get_search_contacts(limit: int, offset: int,
                              db: Session,
                              user: User,
                              contact_first_name: str | None = None,
                              contact_last_name: str | None = None
                              ) -> list[Contact]:
    """
    The get_search_contacts function searches for contacts in the database.
        It takes a limit and offset to paginate through results, as well as a user object to identify which user's contacts are being searched.
        The function also takes optional contact_first_name and contact_last_name arguments that can be used to filter the search results.

    :param limit: int: Limit the number of results returned
    :param offset: int: Specify the number of rows to skip
    :param db: Session: Pass the database session to the function
    :param user: User: Identify the user who is making the request
    :param contact_first_name: str | None: Filter the contacts by first name
    :param contact_last_name: str | None: Filter the contacts by last name
    :return: A list of contact objects
    :rtype: list[Contact]
    """
    contacts = db.query(Contact).filter_by(user_id=user.id)
    if contact_first_name:
        contacts = contacts.filter_by(contact_first_name=contact_first_name)
    if contact_last_name:
        contacts = contacts.filter_by(contact_last_name=contact_last_name)
    return contacts.limit(limit).offset(offset).all()


async def get_contact_by_email(user_email: str, db: Session, user: User) -> Contact | None:
    """
    The get_contact_by_email function takes in a user_email and returns the contact associated with that email.
        If no such contact exists, it returns None.

    :param user_email: str: Pass the email of the contact to be retrieved
    :param db: Session: Access the database
    :param user: User: Get the user_id from the user object
    :return: A contact object
    :rtype: Contact | None
    """
    contact = db.query(Contact).filter(and_(Contact.user_id == user.id, Contact.email == user_email)).first()
    return contact


async def create_contact(body: ContactModel, db: Session, user: User) -> Contact:
    """
    The create_contact function creates a new contact in the database.

    :param body: ContactModel: Create a new contact object
    :param db: Session: Access the database
    :param user: User: Get the user id from the token
    :return: A contact object
    :rtype: Contact
    """
    contact = Contact(**body.dict())
    contact.user_id = user.id
    db.add(contact)
    db.commit()
    return contact


async def update_contact(contact_id: int, body: ContactModel, db: Session, user: User) -> Contact:
    """
    The update_contact function updates a contact in the database.
        Args:
            contact_id (int): The id of the contact to update.
            body (ContactModel): The updated information for the specified user.

    :param contact_id: int: Identify the contact that is to be deleted
    :param body: ContactModel: Get the information from the request body
    :param db: Session: Get the database session
    :param user: User: Make sure that the user is only able to delete their own contacts
    :return: A contact object
    :rtype: Contact
    """
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


async def delete_contact(contact_id: int, db: Session, user: User) -> Contact | None:
    """
    The delete_contact function deletes a contact from the database.
        Args:
            user_id (int): The id of the contact to be deleted.
            db (Session): A connection to the database.

    :param contact_id: int: Get the contact by id
    :param db: Session: Pass the database session to the function
    :param user: User: Check if the user is logged in
    :return: The deleted contact (if it exists) or none
    :rtype: Contact | None
    """
    contact = await get_contact_by_id(contact_id, db, user)
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def get_contacts_by_birthday(limit: int, offset: int, db: Session, user: User) -> list[Contact]:
    """
    The get_contacts_by_birthday function returns a list of contacts that have birthdays within the next 7 days.
        The function takes in 3 parameters: limit, offset, and db. Limit is an integer representing how many contacts to return at once.
        Offset is an integer representing where to start returning results from (i.e., if you want to get the second page of results).
        Db is a database session object used for querying the database.

    :param limit: int: Set the maximum number of contacts that can be returned
    :param offset: int: Specify the number of records to skip before starting to return rows
    :param db: Session: Pass the database session to the function
    :param user: User: Get the user_id of the current user
    :return: A list of contacts that have a birthday in the next 7 days
    :rtype: list[UserContact]
    """
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
