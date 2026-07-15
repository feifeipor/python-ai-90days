# def add (a,b):
#     result = a+b
#     print(result)
# add(10,20)
# def add(a, b):
#     result = a + b
#     return result
# number = add(10, 20)
# # print(number)
# def calculate(a,b,operator):
#     if operator == "+":
#         return a+b
#     elif operator == "-":
#         return a-b
#     elif operator == "*":
#         return a*b
#     elif operator == "/":
#         if b == 0:
#             return "不能除以0"
#         return a/b
#     else:
#         return"不支持这个运算"
# result=calculate(10, 5, "*")
# print(result)
def calculate_future_money(now_save, salary_month, expense_month, years):
    # now_save存款, salary薪水, expense支出, years年份
    future_money = now_save + (salary_month - expense_month) * 12 * years
    return future_money #未来资产计算

def calculate_save_rate(salary_month, expense_month):
    rate = (salary_month - expense_month) / salary_month * 100
    return rate

def check_level(future_money):
    if future_money >=1000000:
        return '财富等级：优秀'
    elif future_money >=500000:
        return '财富等级：良好'
    else:
        return '继续努力'
    
now_save = int(input("请输入当前存款："))
salary_month = int(input("请输入每月收入："))
expense_month = int(input("请输入每月支出："))
years = int(input("请输入计划年份："))
future_money = calculate_future_money (now_save,salary_month,expense_month,years)
save_rate = calculate_save_rate (salary_month,expense_month)
level = check_level(future_money)

print(f"未来资产：{future_money}元")
print(f"储蓄率：{save_rate:.0f}%")
print(level)
