def create_report(name, money, income, level, future, growth, multiple, advice, date):
    report = f"""
    ==============================
    💰 Wealth Predictor 财富报告
    ==============================

    用户信息
    ------------------------------
    姓名: {name}

    资产情况
    ------------------------------
    当前资产: {money:,.0f} 元

    月收入: {income:,.0f} 元

    财富分析
    ------------------------------
    财富等级: {level}

    未来10年资产: {future:,.0f} 元

    资产增长: {growth:,.0f} 元

    增长倍数: {multiple:.2f} 倍

    投资建议
    ------------------------------
    {advice}

    报告日期:
    {date}

    ==============================
    """


    print(report)


    filename = f"{name}_财富报告.txt"


    with open(filename, "w", encoding="utf-8") as file:

        file.write(report)


    print(f"报告已经保存:{filename}")