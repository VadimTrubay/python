import os
import sys
import unittest
from unittest.mock import MagicMock

from sqlalchemy.orm import Session

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from goit_web_hw13.database.models import User
from goit_web_hw13.schemas import UserModel
from goit_web_hw13.repository.auth import (
    get_user_by_email,
    create_user,
    update_token,
    confirmed_email,
    update_avatar,
)


class TestContacts(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.session = MagicMock(spec=Session)
        self.user = User(id=1)

    async def test_get_user_by_email_found(self):
        user = User()
        self.session.query().filter().first.return_value = user
        result = await get_user_by_email(email='', db=self.session)
        self.assertEqual(result, user)

    async def test_get_user_by_email_not_found(self):
        self.session.query().filter().first.return_value = None
        result = await get_user_by_email(email='', db=self.session)
        self.assertIsNone(result)

    async def test_create_user(self):
        body = UserModel(
            username='test1',
            email='Emai@lStr.bg',
            password='testpass',
        )
        result = await create_user(body, db=self.session)
        self.assertEqual(result.username, body.username)
        self.assertEqual(result.email, body.email)
        self.assertTrue(hasattr(result, "id"))
        self.assertTrue(hasattr(result, "created_at"))
        self.assertTrue(hasattr(result, "avatar"))

    async def test_update_token(self):
        await update_token(self.user, 'new_token', db=self.session)
        self.assertEqual(self.user.refresh_token, 'new_token')

    async def test_confirmed_email(self):
        self.user.email = 'test@mail.com'
        self.session.query().filter().first.return_value = self.user
        await confirmed_email(email=self.user.email, db=self.session)
        self.assertTrue(self.user.confirmed)

    async def test_update_avatar(self):
        self.user.email = 'test@mail.com'
        avatar_url = 'http/test/avatar.png'
        self.session.query().filter().first.return_value = self.user
        await update_avatar(email=self.user.email, url=avatar_url, db=self.session)
        self.assertEqual(self.user.avatar, avatar_url)


if __name__ == "__main__":
    unittest.main()
