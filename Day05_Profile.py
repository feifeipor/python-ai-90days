# name = input('请输入名字：')
# age = int(input('请输入年龄；'))
# city = input("请输入城市：")
# job = input('请输入职业：')
# salary = float(input('请输入收入：'))
# hobby = input('请输入爱好：')
# money = 500000
# print(
#     f"""
# 个人信息：
#
# 姓名：{name}
# 年龄：{age}
# 城市：{city}
# 职业：{job}
# 工资；{salary}
# 爱好；{hobby}
# 目前存款：{money}
# """
# )
# year_save = 100000
# years = 5
# money_total = money + year_save * years
# print(
#     f"""
# 未来资产计算：
# 当前存款：{money}元
# 每年存款：{year_save}元
# 计划年份：{years}年
# 5年后资产：{money_total}元
# """
# )
now_save = float(input('请输入当前存款；'))
salary_month = float(input('请输入每月收入：'))
expense_month = float(input('请输入每月支出；'))
plan_year = int(input('请输入计划年份:'))
future_save =now_save + (salary_month - expense_month) * 12 * plan_year
print(f'计划{plan_year}年后的资产：{future_save}元')
save_rate = (salary_month - expense_month) / salary_month * 100
print(f"你的储蓄率是：{save_rate:.0f}%")
if future_save >100**3 :
    print('财富等级：优秀')
elif future_save <100**3 or future_save >=500000:
    print('财富等级：良好')
else :
    print('继续努力')





