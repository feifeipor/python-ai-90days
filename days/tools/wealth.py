def check_level(money, income):

    if money >= 1000000 and income >= 20000:
        return "财富自由潜力"

    elif money >= 500000:
        return "财富成长阶段"

    elif money >= 100000:
        return "财富起步阶段"

    else:
        return "财富积累阶段"
if __name__ == "__main__":

    print(check_level(1000000, 30000))
    print(check_level(500000, 10000))
    print(check_level(50000, 5000))