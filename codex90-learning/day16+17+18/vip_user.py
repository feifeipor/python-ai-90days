from user import User


class VIPUser(User):


    def show_info(self):

        super().show_info()

        print(
            "VIP等级:黄金会员"
        )