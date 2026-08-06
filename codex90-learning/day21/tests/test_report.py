import os
import tempfile
import unittest

from user import User
from vip_user import VIPUser
from tools.report import create_report


class TestReport(unittest.TestCase):

    def setUp(self):
        self.original_directory = os.getcwd()
        self.temp_directory = tempfile.TemporaryDirectory()
        os.chdir(self.temp_directory.name)

    def tearDown(self):
        os.chdir(self.original_directory)
        self.temp_directory.cleanup()

    def test_create_normal_user_report(self):
        user = User("张三", 10000, 5000)
        future_money = user.predict_future()

        filename = create_report(user, future_money)

        self.assertTrue(os.path.exists(filename))
        self.assertEqual(filename, "reports/张三_report.txt")

        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        self.assertIn("张三", content)
        self.assertIn("10000", content)
        self.assertIn("5000", content)
        self.assertIn("610000", content)
        self.assertIn("user", content)

    def test_create_vip_user_report(self):
        user = VIPUser("李四", 20000, 8000)
        future_money = user.predict_future()

        filename = create_report(user, future_money)

        self.assertTrue(os.path.exists(filename))

        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        self.assertIn("李四", content)
        self.assertIn("vip", content)
        self.assertIn(str(future_money), content)


if __name__ == "__main__":
    unittest.main()