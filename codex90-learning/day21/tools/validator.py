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