import json


FILE = "users.json"


def save_users(users):

    with open(
        FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            users,
            file,
            ensure_ascii=False,
            indent=4
        )


def load_users():

    try:

        with open(
            FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except FileNotFoundError:

        return []