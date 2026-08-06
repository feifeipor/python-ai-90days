import unittest

from user import User
from vip_user import VIPUser
from tools.user_factory import create_user_from_data


class TestUserFactory(unittest.TestCase):

    def test_create_normal_user(self):
        data = {
            "name": "张三",
            "money": 10000,
            "income": 5000,
            "type": "user"
        }

        user = create_user_from_data(data)

        self.assertIsInstance(user, User)
        self.assertNotIsInstance(user, VIPUser)
        self.assertEqual(user.name, "张三")
        self.assertEqual(user.money, 10000)
        self.assertEqual(user.income, 5000)

    def test_create_vip_user(self):
        data = {
            "name": "李四",
            "money": 20000,
            "income": 8000,
            "type": "vip"
        }

        user = create_user_from_data(data)

        self.assertIsInstance(user, VIPUser)
        self.assertEqual(user.name, "李四")
        self.assertEqual(user.money, 20000)
        self.assertEqual(user.income, 8000)
        self.assertEqual(user.type, "vip")

    def test_created_user_can_predict(self):
        data = {
            "name": "王五",
            "money": 10000,
            "income": 5000,
            "type": "user"
        }

        user = create_user_from_data(data)

        self.assertEqual(user.predict_future(), 610000)


if __name__ == "__main__":
    unittest.main()