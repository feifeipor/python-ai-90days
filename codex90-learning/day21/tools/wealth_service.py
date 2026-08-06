from tools.database import load_users

from user import User
from vip_user import VIPUser

from tools.validator import check_users, get_user_index
from tools.report import create_report

def predict_wealth() -> None:

    users = load_users()

    if not check_users(users):
        return


    print("================")


    for index, item in enumerate(users):

        print(
            index,
            item["name"]
        )

    index = get_user_index(users)

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