class User:


    def __init__(self, name, money):

        self.name = name

        self.money = money



    def show_report(self):

        print(
            f"{self.name}普通财富报告"
        )



class VIPUser(User):


    def show_report(self):

        super().show_report()

        print(
            "增加VIP投资分析"
        )



user1 = User(
    "张三",
    50000
)


user2 = VIPUser(
    "李四",
    100000
)



users = [

    user1,

    user2

]


for user in users:

    user.show_report()