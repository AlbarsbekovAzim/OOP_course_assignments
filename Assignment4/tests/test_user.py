import unittest
from datetime import datetime
from src.user import User
from src.user_service import UserService
from src.user_util import UserUtil


class TestUser(unittest.TestCase):

    def test_get_age(self):
        user = User(1, "John", "Doe", datetime(2000, 1, 1))
        self.assertTrue(user.get_age() >= 24)


class TestUserService(unittest.TestCase):

    def setUp(self):
        UserService.users.clear()
        self.user = User(1, "Alice", "Smith", datetime(1995, 5, 5))
        UserService.add_user(self.user)

    def test_add_user(self):
        self.assertEqual(UserService.get_number(), 1)

    def test_find_user(self):
        self.assertIsNotNone(UserService.find_user(1))

    def test_delete_user(self):
        UserService.delete_user(1)
        self.assertEqual(UserService.get_number(), 0)


class TestUserUtil(unittest.TestCase):

    def test_generate_user_id(self):
        user_id = UserUtil.generate_user_id()
        self.assertEqual(len(str(user_id)), 9)

    def test_password(self):
        password = UserUtil.generate_password()
        self.assertTrue(UserUtil.is_strong_password(password))

    def test_email_validation(self):
        self.assertTrue(UserUtil.validate_email("john.doe@gmail.com"))
        self.assertFalse(UserUtil.validate_email("wrong-email"))


if __name__ == "__main__":
    unittest.main()
