from tools.calculator import predict_money
class User:


    def __init__(self,name,money,income):

        self.name = name
        self.money = money
        self.income = income
        self.type = "user"



    def show_info(self):

        print(f"用户:{self.name}")
        print(f"资产:{self.money}")
        print(f"月收入:{self.income}")



    def predict_future(self):

        return predict_money(
            self.money,
            self.income
        )


    def advice(self):

        return "保持储蓄，提高收入"