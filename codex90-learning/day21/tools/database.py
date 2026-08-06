import json
from tools.log_config import get_logger
from tools.exceptions import DuplicateUserError


logger = get_logger(__name__)

def add_user(user):

    try:
        users_data = load_users()

    except FileNotFoundError:
        users_data = []


    # 检查用户是否存在
    for old_user in users_data:

        if old_user["name"] == user.name:
            logger.warning(
                "Duplicate user rejected: %s",
                user.name
            )

            raise DuplicateUserError(
                f"用户“{user.name}”已存在"
            )


    user_data = {

        "name": user.name,

        "money": user.money,

        "income": user.income,

        "type": user.type

    }
    users_data.append(user_data)


    with open(
            "users.json",
        "w",
        encoding="utf-8"

    ) as file:


        json.dump(
            users_data,
            file,
            ensure_ascii=False,
            indent=4
        )

    logger.info(
        "User saved: name=%s, type=%s",
        user.name,
        user.type
    )

    return True

def load_users():

    with open(
            "users.json",
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    logger.info(
        "Loaded %d users",
        len(data)
    )

    return data

def show_users():

    users = load_users()


    if len(users) == 0:

        print("暂无用户")

        return


    for user in users:

        print("================")

        print(
            f"姓名:{user['name']}"
        )

        print(
            f"资产:{user['money']}"
        )

        print(
            f"收入:{user['income']}"
        )
