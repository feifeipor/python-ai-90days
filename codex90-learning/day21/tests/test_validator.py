import unittest
from unittest.mock import patch

from tools.validator import (
    check_name,
    check_money,
    check_users,
    get_number,
    get_user_type,
    get_menu_choice,
    get_user_index,
)


class TestValidator(unittest.TestCase):

    def test_check_name_valid(self):
        self.assertTrue(check_name("张三"))

    def test_check_name_empty(self):
        self.assertFalse(check_name("   "))

    def test_check_money_valid(self):
        self.assertTrue(check_money(0))
        self.assertTrue(check_money(1000))

    def test_check_money_negative(self):
        self.assertFalse(check_money(-1))

    def test_check_users(self):
        self.assertFalse(check_users([]))
        self.assertTrue(check_users([{"name": "张三"}]))

    @patch("builtins.input", side_effect=["abc", "100"])
    def test_get_number(self, mock_input):
        result = get_number("请输入数字：")
        self.assertEqual(result, 100)

    @patch("builtins.input", side_effect=["3", "2"])
    def test_get_user_type(self, mock_input):
        result = get_user_type()
        self.assertEqual(result, "2")

    @patch("builtins.input", side_effect=["8", " 3 "])
    def test_get_menu_choice(self, mock_input):
        result = get_menu_choice()
        self.assertEqual(result, "3")

    @patch("builtins.input", side_effect=["abc", "-1", "99", "1"])
    def test_get_user_index(self, mock_input):
        users = [
            {"name": "用户1"},
            {"name": "用户2"},
        ]

        result = get_user_index(users)
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()