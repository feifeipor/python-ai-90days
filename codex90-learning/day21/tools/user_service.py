from user import User
from vip_user import VIPUser
from tools.database import load_users, add_user
from tools.validator import (
    check_name,
    check_money,
    check_users,
    get_number,
    get_user_type
)
from tools.exceptions import DuplicateUserError

def add_new_user() -> None:

    name = input("请输入姓名:")
    if not check_name(name):
        print("姓名不能为空")
        return

    money = get_number("请输入资产:")
    if not check_money(money):
        print("资产不能小于0")
        return

    income = get_number("请输入月收入:")
    if not check_money(income):
        print("收入不能小于0")
        return


    print("请选择用户类型")

    print("1. 普通用户")

    print("2. VIP用户")


    user_type = get_user_type()

    USER_CLASSES = {
        "1": User,
        "2": VIPUser
    }

    user_class = USER_CLASSES[user_type]

    user = user_class(
        name,
        money,
        income
    )

    try:
        add_user(user)

    except DuplicateUserError as error:
        print(error)
        return

    print("用户添加成功")

def show_users() -> None:

    users = load_users()

    if not check_users(users):

        return

    else:

        print("================")


        for item in users:

            print(
                f"用户:{item['name']}"
            )

            print(
                f"资产:{item['money']}"
            )

            print(
                f"收入:{item['income']}"
            )

            print("================")