from tools.wealth import check_level
from tools.money import future_money


print("-----欢迎使用财富预测器-----")

name = input("请输出姓名：")
money = int(input("请输入当前资产: "))
income = int(input("请输入月收入: "))


level = check_level(money, income)

print("------------------------")
print("--------财富报告----------")
print("------------------------")
print(f'姓名： {name}')
print(f'当前资产； {money}')
print(f'月收入：{income}')
print("财富等级:", level)

future = future_money(money,income,10)

print(f"10年后预计资产: {future:.0f} 元")

growth = future - money #增长金额
multiple = future / money #增长倍数

print(f"资产增长: {growth:.0f} 元")
print(f"增长倍数: {multiple:.2f} 倍")

from tools.advice import get_advice

advice = get_advice(money,income)

print("投资建议:", advice)

from datetime import datetime

today = datetime.now()

print("报告日期：", today)

print("------------------------")