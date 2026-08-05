from user import User
from vip_user import VIPUser
from tools.database import add_user
from tools.report import create_report
from tools.validator import (get_number, check_name, check_money, check_users)

def add_new_user():

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


    user_type = input("请选择:")


    if user_type == "2":

        user = VIPUser(
            name,
            money,
            income
        )


    else:

        user = User(
            name,
            money,
            income
        )


    result = add_user(user)


    if result:

        print("用户添加成功")

    else:

        print("用户已存在")

def show_users():

    from tools.database import load_users

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

def predict_wealth():

    from tools.database import load_users
    from user import User
    from vip_user import VIPUser


    users = load_users()

    if not check_users(users):
        return


    print("================")


    for index, item in enumerate(users):

        print(
            index,
            item["name"]
        )


    index = int(
        input("请选择用户编号:")
    )


    user_data = users[index]


    if user_data["type"] == "vip":

        user = VIPUser(
            user_data["name"],
            user_data["money"],
            user_data["income"]
        )

    else:

        user = User(
            user_data["name"],
            user_data["money"],
            user_data["income"]
        )


    future = user.predict_future()


    print(
        f"{user.name}未来10年资产:{future}"
    )

    create_report(
        user,
        future
    )

def run_system():

    while True:

        print("================")
        print("财富预测系统")
        print("================")

        print("1. 添加用户")
        print("2. 查看用户")
        print("3. 财富预测")
        print("4. 退出")

        choice = input("请选择:")

        if choice == "1":

            add_new_user()

        elif choice == "2":

            show_users()

        elif choice == "3":

            predict_wealth()

        elif choice == "4":

            print("程序退出")

            break