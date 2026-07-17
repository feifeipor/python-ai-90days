# 💰 Wealth Predictor
# 个人财富预测与分析系统


from tools.calculator import *
from tools.money import *
from tools.wealth import *
from tools.advice import *
from tools.report import *
from tools.database import add_user, get_users
from datetime import datetime


print("""
=============================
       💰 Wealth Predictor
=============================

1. 财富分析
2. 查看历史记录

=============================
""")


choice = input("请选择功能：")


# ============================
# 财富分析
# ============================

if choice == "1":

    print("\n请输入个人财务信息，生成未来财富预测报告\n")


    name = input("请输入姓名：")

    money = int(
        input("请输入当前资产：")
    )

    income = int(
        input("请输入月收入：")
    )


    # 保存用户数据

    user = {

        "name": name,

        "money": money,

        "income": income

    }


    add_user(user)



    # 财富等级分析

    level = check_level(
        money,
        income
    )


    # 财富增长预测

    future_asset = future_money(
        money,
        income,
        10
    )


    # 增长金额

    growth = future_asset - money


    # 增长倍数

    multiple = round(
        future_asset / money,
        2
    )


    # 投资建议

    suggestion = get_advice(
        money,
        income
    )



    # 输出报告

    print("\n")
    print("=============================")
    print("💰 Wealth Predictor 财富报告")
    print("=============================")


    print("\n用户信息")
    print("-----------------------------")

    print(
        f"姓名: {name}"
    )


    print("\n资产情况")
    print("-----------------------------")

    print(
        f"当前资产: {money:,} 元"
    )

    print(
        f"月收入: {income:,} 元"
    )


    print("\n财富分析")
    print("-----------------------------")


    print(
        f"财富等级: {level}"
    )


    print(
        f"未来10年资产预测: {future_asset:,} 元"
    )


    print(
        f"资产增长: {growth:,} 元"
    )


    print(
        f"增长倍数: {multiple} 倍"
    )


    print("\n投资建议")
    print("-----------------------------")


    print(
        suggestion
    )



    # 自动生成报告文件

    from datetime import datetime

    create_report(
        name,
        money,
        income,
        level,
        future_asset,
        growth,
        multiple,
        suggestion,
        datetime.now().strftime("%Y-%m-%d")
    )


    print("\n报告已经生成完成！")



# ============================
# 查看历史记录
# ============================

elif choice == "2":


    users = get_users()


    print("\n")
    print("=============================")
    print("📂 历史用户记录")
    print("=============================")


    if len(users) == 0:

        print(
            "暂无历史数据"
        )


    else:

        for index, user in enumerate(
            users,
            start=1
        ):


            print(
                f"""
用户 {index}

姓名:
{user['name']}

当前资产:
{user['money']:,} 元

月收入:
{user['income']:,} 元

-----------------------------
"""
            )


else:

    print(
        "输入错误，请重新运行程序"
    )