from database import load_users, save_users


def add_user():

    users = load_users()


    name = input(
        "请输入用户名:"
    )


    age = int(
        input(
            "请输入年龄:"
        )
    )


    user = {

        "name":name,

        "age":age

    }


    users.append(user)


    save_users(users)


    print("添加成功")



def show_users():

    users = load_users()


    for user in users:

        print(
            f"姓名:{user['name']}"
        )

        print(
            f"年龄:{user['age']}"
        )
