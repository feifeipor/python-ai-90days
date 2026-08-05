class User:


    def show_info(self):

        print("普通用户")


class VIPUser(User):


    def show_info(self):

        print("VIP用户")


user1 = User()

user2 = VIPUser()


users = [
    user1,
    user2
]


for user in users:

    user.show_info()