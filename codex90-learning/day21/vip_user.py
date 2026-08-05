from user import User

class VIPUser(User):
    def __init__(self, name, money, income):

        super().__init__(name,money,income)
        self.type = "vip"

    def show_info(self):
        super().show_info()
        print("VIP财富建议：增加投资规划")

    def predict_future(self):
        future_money = (self.money+self.income * 12 * 10)
        future_money = future_money * 1.1

        return int(future_money)

    def advice(self):

        return "增加投资规划，提高资产增长"