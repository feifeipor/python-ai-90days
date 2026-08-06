import os
import tempfile
import unittest

from user import User
from vip_user import VIPUser
from tools.database import (
    add_user,
    load_users,
)


class TestDatabase(unittest.TestCase):

    def setUp(self):
        """每个测试开始前，进入一个全新的临时目录。"""
        self.original_directory = os.getcwd()
        self.temp_directory = tempfile.TemporaryDirectory()
        os.chdir(self.temp_directory.name)

    def tearDown(self):
        """每个测试结束后，恢复原目录并删除临时文件。"""
        os.chdir(self.original_directory)
        self.temp_directory.cleanup()

    def test_add_first_user_creates_file(self):
        user = User("张三", 10000, 5000)

        result = add_user(user)

        self.assertTrue(result)
        self.assertTrue(os.path.exists("users.json"))

        users = load_users()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0]["name"], "张三")
        self.assertEqual(users[0]["type"], "user")

    def test_add_vip_user(self):
        user = VIPUser("李四", 20000, 8000)

        self.assertTrue(add_user(user))

        users = load_users()
        self.assertEqual(users[0]["type"], "vip")

    def test_duplicate_name_is_rejected(self):
        first_user = User("张三", 10000, 5000)
        duplicate_user = VIPUser("张三", 50000, 10000)

        self.assertTrue(add_user(first_user))
        self.assertFalse(add_user(duplicate_user))

        users = load_users()
        self.assertEqual(len(users), 1)

if __name__ == "__main__":
    unittest.main()