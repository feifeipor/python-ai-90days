class User:


    def __init__(self,name,money,age):

        self.name = name

        self.money = money

        self.age = age



    def show_info(self):

        print(
            f"用户:{self.name}"
        )

        print(
            f"资产:{self.money}"
        )

        print(
            f"年龄:{self.age}"
        )

    def add_money(self, money):
        self.money = self.money + money

user1 = User(
    "飞飞",
    50000,
    30
)


user1.show_info()

print("----------------")


user1.add_money(10000)


user1.show_info()