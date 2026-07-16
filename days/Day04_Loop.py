# total = 0
# for i in range(1,101):
#     total = total + i
# print(total)
# record = ["午餐", 22.5, "餐饮"]
# print(record)
# record = {
#     "name":'午餐',
#     "amount":22.5,
#     "category":'餐饮'
# }
# print(record["amount"])
# records = [
#     # {"name": "午餐", "amount": 22.5, "category": "餐饮"},
#     # {"name": "公交", "amount": 2.0, "category": "交通"},
#     # {'name':'衣服','amount':60.0,'category':'购物“'},
# ]
# for record in records:
#     print(record["amount"])
records = [ ]
again = "y"
while again == "y":
    name = input("请输入消费项目：")
    amount = float(input("请输入金额："))
    category = input("请输入类别：")
    record = {
        "name":name,
        "amount":amount,
        "category":category
    }
    records.append(record)
    again = input("继续录入吗？输入 y 继续：")
total = 0
count = 0
for record in records:
    total = total+record["amount"]
    count = count+1
average = total/count
print("总支出：", total)
print("平均支出：", round(average, 2))
max_amount = 0
for record in records:
    if record["amount"] > max_amount:
        max_amount = record["amount"]
print("最大支出：",max_amount )
# transport_total = 0
# for record in records:
#     if record["category"]== "交通":
#         transport_total = transport_total + record["amount"]
# print("交通支出：", transport_total)
category_totals = {}
for record in records:
    category = record["category"]
    if category not in category_totals:
        category_totals[category] = 0
    category_totals[category] = category_totals[category] + record["amount"]
print("分类统计：")
for category in category_totals:
    print(category, "：",category_totals[category])