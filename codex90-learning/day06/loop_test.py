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

    print(
        f"资产:{user['money']}元"
    )
