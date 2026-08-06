import os
from datetime import datetime

def create_report(user, future_money):

    content = f"""
    ====================
    财富分析报告
    ====================

    用户:
    {user.name}

    用户等级:
    {user.type}

    当前资产:
    {user.money}

    月收入:
    {user.income}

    未来10年预测资产:
    {future_money}
    
    财富建议:
    {user.advice()}

    生成时间:
    {datetime.now().strftime("%Y-%m-%d")}

    ====================
    """

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/{user.name}_report.txt"


    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(content)


    print("报告生成成功")

    return filename

