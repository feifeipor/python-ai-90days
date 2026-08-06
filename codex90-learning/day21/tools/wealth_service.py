from tools.database import load_users

from user import User
from vip_user import VIPUser

from tools.validator import check_users
from tools.report import create_report

def predict_wealth():

    users = load_users()

    if not check_users(users):
        return


    print("================")


    for index, item in enumerate(users):

        print(
            index,
            item["name"]
        )

    try:
        index = int(
            input("请选择用户编号:")
        )

    except ValueError:
        print("输入错误，请输入数字编号")
        return

    if index < 0 or index >= len(users):
        print("用户编号不存在")
        return

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