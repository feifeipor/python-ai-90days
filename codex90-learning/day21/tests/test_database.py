import os
import tempfile
import unittest

from user import User
from vip_user import VIPUser
from tools.database import (add_user,load_users,)
from tools.exceptions import DuplicateUserError


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
        with self.assertRaises(DuplicateUserError):
            add_user(duplicate_user)

        users = load_users()
        self.assertEqual(len(users), 1)

    def test_load_users_when_file_missing(self):
        users = load_users()

        self.assertEqual(users, [])

    def test_load_users_when_file_empty(self):
        with open(
                "users.json",
                "w",
                encoding="utf-8"
        ):
            pass

        users = load_users()

        self.assertEqual(users, [])

    def test_load_users_when_json_is_invalid(self):
        with open(
                "users.json",
                "w",
                encoding="utf-8"
        ) as file:
            file.write("{invalid json")

        users = load_users()

        self.assertEqual(users, [])

    def test_load_users_when_data_is_not_a_list(self):
        with open(
                "users.json",
                "w",
                encoding="utf-8"
        ) as file:
            file.write('{"name": "张三"}')

        users = load_users()

        self.assertEqual(users, [])

if __name__ == "__main__":
    unittest.main()