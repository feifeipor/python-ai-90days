# 智能建议
def get_advice(money, income):

    if money >= 1000000:
        return "资产达到百万级，可以考虑资产配置"

    elif income < 5000:
        return "收入偏低，建议提升技能增加收入"

    else:
        return "保持储蓄习惯，持续提高收入"


if __name__ == "__main__":
    print(get_advice(500000,10000))