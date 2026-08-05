from user import add_user,show_users


while True:


    print(
"""
================

用户管理系统

1. 添加用户

2. 查看用户

3. 退出

================
"""
    )


    choice = input(
        "请选择:"
    )


    if choice == "1":

        add_user()


    elif choice == "2":

        show_users()


    elif choice == "3":

        print("退出")

        break


    else:

        print("输入错误")