try:

    money = int(
        input("请输入当前资产:")
    )

    print(
        f"你的资产是{money}元"
    )


except ValueError:

    print("请输入数字")

finally:

    print("程序结束")