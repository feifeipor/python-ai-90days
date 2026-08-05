import json
from user import User
from vip_user import VIPUser

def save_users(users):

    data = []


    for user in users:

        user_data = {
        "name": user.name,
        "money": user.money,
        "income": user.income,
        "type": "vip" if isinstance(user, VIPUser) else "user" }

        data.append(user_data)


    with open(
        "users.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )

class User:
    def __init__(self, name, money, income):
        self.name = name

        self.money = money

        self.income = income

    def show_info(self):
        print(
            f"用户:{self.name}"
        )

        print(
            f"资产:{self.money}"
        )

        print(
            f"月收入:{self.income}"
        )

    def predict_future(self):
        future_money = self.money + self.income * 12 * 10

        return future_money

user1 = User(
    "飞飞",
    50000,
    5000
)


user1.show_info()


future = user1.predict_future()



class VIPUser(User):

    def vip_advice(self):

        print("VIP财富建议：增加投资规划")

    def predict_future(self):
        future_money = self.money + self.income * 12 * 10

        future_money = future_money * 1.1

        return int(future_money)

vip_user = VIPUser(
    "李四",
    100000,
    10000
)

vip_user.show_info()
vip_user.vip_advice()


users = [user1,vip_user]
save_users(users)

for user in users:
    print(
        f"{user.name}未来10年资产:{user.predict_future()}"
    )

def load_users():

    users = []

    with open(
        "users.json",
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)


    for item in data:

        if item["type"] == "vip":

            user = VIPUser(
                item["name"],
                item["money"],
                item["income"]
            )

        else:

            user = User(
                item["name"],
                item["money"],
                item["income"]
            )


        users.append(user)


    return users

def create_users(data):

    users = []

    for item in users_data:

        if item["type"] == "vip":

            user = VIPUser(
                item["name"],
                item["money"],
                item["income"]
            )

        else:

            user = User(
                item["name"],
                item["money"],
                item["income"]
            )

        users.append(user)


users_data = load_users()


new_users = create_users(users_data)


for user in new_users:

    user.show_info()

print(users_data)

import json


with open(
    "users.json",
    "r",
    encoding="utf-8"
) as file:

    users_data = json.load(file)


print(users_data)

for user in users_data:
    if user["type"] == "vip":

        print(
            "这是VIP用户"
        )

    else:

        print(
            "这是普通用户"
        )
    print(user)