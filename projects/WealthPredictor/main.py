from tools.wealth import check_level
from tools.money import future_money

print("==============================")
print("💰 Wealth Predictor")
print("==============================")
print("请输入个人财务信息，生成未来财富预测报告")
print()
name = input("请输出姓名：")
money = int(input("请输入当前资产: "))
income = int(input("请输入月收入: "))

level = check_level(money, income)

future = future_money(money,income,10)

growth = future - money #增长金额
multiple = future / money #增长倍数

from tools.advice import get_advice

advice = get_advice(money,income)

from datetime import datetime

date = datetime.now().strftime("%Y-%m-%d")

from tools.report import create_report
create_report(
    name,
    money,
    income,
    level,
    future,
    growth,
    multiple,
    advice,
    date
)
from tools.database import add_user
user = {
    "name": name,
    "money": money,
    "income": income
}


add_user(user)