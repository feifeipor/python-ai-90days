# cash=1000000
# expence=50000
# left=cash-expence
# print(left)
# name = input("请输入名字:")
# print("你好", name)
# #input得到的数据默认是：字符串！
# money = float(input("请输入金额:"))
#=========今日练习===========
#个人财务计算器
Shouru=float(input('今天收入多少：'))
Zhichu=float(input('今天支出多少：'))
cash=Shouru-Zhichu
print(f'今天收入为{cash}元')
Ace=f'{(cash/Shouru)*100:.2f}%'
print(f"储蓄率为{Ace}")
