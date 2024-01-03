import unittest
from unittest.mock import MagicMock

from sqlalchemy import and_
from sqlalchemy.orm import Session

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from contacts.database.models import Contact, User
from contacts.schemas import ContactModel
from contacts.repository.contacts import (
    get_contacts,
    get_contact_by_id,
    get_search_contacts,
    get_contacts_by_birthday,
    get_contact_by_email,
    create_contact,
    delete_contact,
    update_contact,
    )


class TestContacts(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.session = MagicMock(spec=Session)
        self.user = User(id=1)

    async def test_get_contacts(self):
        contacts = [Contact(), Contact(), Contact()]
        self.session.query().filter_by().limit().offset().all.return_value = contacts
        result = await get_contacts(limit=10, offset=0, db=self.session, user=self.user)
        self.assertEqual(result, contacts)

    async def test_get_search_contacts_for_first_name(self):
        contacts = [Contact(), Contact(), Contact()]
        self.session.query().filter_by().filter_by().filter_by().limit().offset().all.return_value = [contacts[0]]
        result = await get_search_contacts(limit=10, offset=0, db=self.session, 
                                           user=self.user, contact_first_name='f',
                                           contact_last_name='l')
        self.assertEqual(result, [contacts[0]])

    async def test_get_search_contacts_for_first_name(self):
        contacts = [Contact(), Contact(), Contact()]
        self.session.query().filter_by().filter_by().limit().offset().all.return_value = [contacts[0]]
        result = await get_search_contacts(limit=10, offset=0, db=self.session, 
                                           user=self.user, contact_first_name='f',
                                           contact_last_name='')
        self.assertEqual(result, [contacts[0]])

    async def test_get_search_contacts_for_first_name_not_found(self):
        contacts = [Contact(), Contact(), Contact()]
        self.session.query().filter_by().filter_by().limit().offset().all.return_value = None
        result = await get_search_contacts(limit=10, offset=0, db=self.session, 
                                           user=self.user, contact_first_name='f',
                                           contact_last_name='')
        self.assertIsNone(result)

    async def test_get_search_contacts_for_last_name(self):
        contacts = [Contact(), Contact(), Contact()]
        self.session.query().filter_by().filter_by().limit().offset().all.return_value = [contacts[0]]
        result = await get_search_contacts(limit=10, offset=0, db=self.session, 
                                           user=self.user, contact_first_name='',
                                           contact_last_name='l')
        self.assertEqual(result, [contacts[0]])

    async def test_get_search_contacts_for_last_name_not_found(self):
        contacts = [Contact(), Contact(), Contact()]
        self.session.query().filter_by().filter_by().limit().offset().all.return_value = None
        result = await get_search_contacts(limit=10, offset=0, db=self.session, 
                                           user=self.user, contact_first_name='',
                                           contact_last_name='l')
        self.assertIsNone(result)

    async def test_get_search_contacts_without_name_last_name(self):
        contacts = [Contact(), Contact(), Contact()]
        self.session.query().filter_by().limit().offset().all.return_value = contacts
        result = await get_search_contacts(limit=10, offset=0, db=self.session, 
                                           user=self.user, contact_first_name='',
                                           contact_last_name='')
        self.assertEqual(result, contacts)

    async def test_get_search_contacts_for_name_last_name_not_found(self):
        contacts = [Contact(), Contact(), Contact()]
        self.session.query().filter_by().filter_by().filter_by().limit().offset().all.return_value = None
        result = await get_search_contacts(limit=10, offset=0, db=self.session, 
                                           user=self.user, contact_first_name='f',
                                           contact_last_name='l')
        self.assertIsNone(result)

    async def test_get_contact_found(self):
        contact = Contact()
        self.session.query().filter().first.return_value = contact
        result = await get_contact_by_id(contact_id=1, user=self.user, db=self.session)
        self.assertEqual(result, contact)

    async def test_get_contact_not_found(self):
        self.session.query().filter().first.return_value = None
        result = await get_contact_by_id(contact_id=1, user=self.user, db=self.session)
        self.assertIsNone(result)

    async def test_get_contact_by_email_found(self):
        contact = Contact()
        self.session.query().filter(and_(True, )).first.return_value = contact
        result = await get_contact_by_email(user_email='em', user=self.user, db=self.session)
        self.assertEqual(result, contact)

    async def test_get_contact_by_email_not_found(self):
        contact = Contact()
        self.session.query().filter(and_(True, )).first.return_value = None
        result = await get_contact_by_email(user_email='em', user=self.user, db=self.session)
        self.assertIsNone(result)

    async def test_create_contact(self):
        body = ContactModel(
            first_name="test",
            last_name="lasttest",
            email="test@test.com",
            phone="+38(065)754-35-75",
            birthday="2020-05-06",
            information="test contact",
        )
        result = await create_contact(body=body, db=self.session, user=self.user)
        self.assertEqual(result.first_name, body.first_name)
        self.assertEqual(result.last_name, body.last_name)
        self.assertEqual(result.email, body.email)
        self.assertEqual(result.phone, body.phone)
        self.assertEqual(result.birthday, body.birthday)
        self.assertEqual(result.information, body.information)
        self.assertEqual(result.user_id, self.user.id)
        self.assertTrue(hasattr(result, "id"))
        self.assertTrue(hasattr(result, "created_at"))
        self.assertTrue(hasattr(result, "updated_at"))

    async def test_remove_contact_found(self):
        contact = Contact()
        self.session.query().filter().first.return_value = contact
        result = await delete_contact(contact_id=1, db=self.session, user=self.user)
        self.assertEqual(result, contact)

    async def test_remove_contact_not_found(self):
        self.session.query().filter().first.return_value = None
        result = await delete_contact(contact_id=1, db=self.session, user=self.user)
        self.assertIsNone(result)

    async def test_update_contact_found(self):
        body = ContactModel(
            first_name="test",
            last_name="lasttest",
            email="test@test.com",
            phone="+38(065)754-35-75",
            birthday="2020-05-06",
            information="test contact",
        )
        contact = Contact()
        self.session.query().filter().first.return_value = contact
        self.session.commit.return_value = None
        result = await update_contact(contact_id=1, body=body, db=self.session, user=self.user)
        self.assertEqual(result, contact)

    async def test_update_contact_not_found(self):
        body = ContactModel(
            first_name="test",
            last_name="lasttest",
            email="test@test.com",
            phone="+38(065)754-35-75",
            birthday="2020-05-06",
            information="test contact",
        )
        self.session.query().filter().first.return_value = None
        self.session.commit.return_value = None
        result = await update_contact(contact_id=1, body=body, db=self.session, user=self.user)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
