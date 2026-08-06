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

def get_menu_choice():
    while True:
        choice = input("请选择：").strip()

        if choice in ("1", "2", "3", "4"):
            return choice

        print("输入错误，请输入1、2、3或4")

def get_user_index(users):
    while True:
        user_input = input("请选择用户编号：").strip()

        try:
            index = int(user_input)
        except ValueError:
            print("输入错误，请输入数字编号")
            continue

        if 0 <= index < len(users):
            return index

        print("用户编号不存在")