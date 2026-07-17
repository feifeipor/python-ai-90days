import json
import os


FILE_PATH = "data/users.json"


def add_user(user):

    users = []

    if os.path.exists(FILE_PATH):

        with open(FILE_PATH,"r",encoding="utf-8") as f:
            users=json.load(f)


    users.append(user)


    with open(FILE_PATH,"w",encoding="utf-8") as f:
        json.dump(
            users,
            f,
            ensure_ascii=False,
            indent=4
        )


def get_users():

    with open(
        FILE_PATH,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)