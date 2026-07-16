# 财富等级判断
# money = int(input("请输入当前资产: "))
# income = int(input("请输入月收入: "))
#
# if money >= 1000000 and income >= 20000:
#     print("财富等级；自由潜力")
#
# elif money >= 500000:
#     print("财富等级；成长阶段")
#
# elif money >= 100000:
#     print("财富等级；起步阶段")
#
# else:
#     print("财富等级；积累阶段")
from tools.wealth import check_level

money = int(input("请输入当前资产: "))
income = int(input("请输入月收入: "))

level = check_level(money, income)

print("财富等级:", level)