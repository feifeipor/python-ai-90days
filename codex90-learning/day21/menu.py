from tools.user_service import add_new_user, show_users
from tools.wealth_service import predict_wealth
from tools.validator import get_menu_choice

def show_menu() -> None:

    MENU_ACTIONS = {
        "1": add_new_user,
        "2": show_users,
        "3": predict_wealth
    }

    while True:

        print("================")
        print("财富预测系统")
        print("================")

        print("1. 添加用户")
        print("2. 查看用户")
        print("3. 财富预测")
        print("4. 退出")

        choice = get_menu_choice()

        if choice == "4":
            print("程序退出")

            break

        MENU_ACTIONS[choice]()

