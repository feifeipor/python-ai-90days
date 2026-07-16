def future_money(current_money, save_money, years,rate=0.05):
    """
    计算未来资产
    """

    total = current_money

    for i in range(years):

        total=total * (1 + rate)
        total += save_money * 12

    return total