import unittest

from user import User
from vip_user import VIPUser


class TestUser(unittest.TestCase):

    def test_user_attributes(self):
        user = User("张三", 10000, 5000)

        self.assertEqual(user.name, "张三")
        self.assertEqual(user.money, 10000)
        self.assertEqual(user.income, 5000)
        self.assertEqual(user.type, "user")

    def test_user_prediction(self):
        user = User("张三", 10000, 5000)

        self.assertEqual(user.predict_future(), 610000)

    def test_user_advice_returns_text(self):
        user = User("张三", 10000, 5000)

        self.assertIsInstance(user.advice(), str)
        self.assertTrue(user.advice())


class TestVIPUser(unittest.TestCase):

    def test_vip_inherits_user(self):
        vip_user = VIPUser("李四", 10000, 5000)

        self.assertIsInstance(vip_user, User)
        self.assertEqual(vip_user.type, "vip")

    def test_vip_attributes(self):
        vip_user = VIPUser("李四", 10000, 5000)

        self.assertEqual(vip_user.name, "李四")
        self.assertEqual(vip_user.money, 10000)
        self.assertEqual(vip_user.income, 5000)

    def test_vip_prediction_has_bonus(self):
        vip_user = VIPUser("李四", 10000, 5000)

        self.assertEqual(vip_user.predict_future(), 671000)


if __name__ == "__main__":
    unittest.main()