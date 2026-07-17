import json
import os


DATA_FILE = "data/users.json"


def load_users():
    """
    读取用户数据
    """
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_users(users):
    """
    保存用户数据
    """
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(
            users,
            file,
            ensure_ascii=False,
            indent=4
        )


def add_user(user):
    """
    添加用户记录
    """
    users = load_users()

    users.append(user)

    save_users(users)