from database import save_users, load_users


users = [

    {
        "name":"飞飞",
        "age":30
    },

    {
        "name":"小明",
        "age":25
    }

]


save_users(users)


data = load_users()


print(data)