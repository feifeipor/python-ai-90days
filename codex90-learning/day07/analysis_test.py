users = [

    {
        "name": "飞飞",
        "money": 50000
    },


    {
        "name": "小明",
        "money": 80000
    },


    {
        "name": "小红",
        "money": 30000
    }

]


for user in users:

    print(
        f"用户:{user['name']}"
    )


    if user["money"] >= 50000:

        print("财富成长阶段")


    else:

        print("继续努力")


    print("----------------")