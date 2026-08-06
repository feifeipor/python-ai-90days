def get_number(message):

    while True:

        try:
            number = int(
                input(message)
            )
            return number


        except ValueError:
            print("请输入数字")

def check_name(name):

    if name.strip() == "":
        return False

    return True

def check_money(number):

    if number < 0:
        return False

    return True

def check_users(users):

    if len(users) == 0:
        print("暂无用户记录")
        return False


    return True

def get_user_type():
    while True:
        user_type = input("请选择：")

        if user_type in ("1", "2"):
            return user_type

        print("输入错误，请输入1或2")