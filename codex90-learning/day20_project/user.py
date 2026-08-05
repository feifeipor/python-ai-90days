class User:


    def __init__(self,name,money):

        self.name = name

        self.money = money



    def show_info(self):

        print(
            f"用户:{self.name}"
        )

        print(
            f"资产:{self.money}"
        )