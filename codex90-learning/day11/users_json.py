import json


users = [

    {
        "name":"飞飞",
        "money":50000
    },

    {
        "name":"小明",
        "money":80000
    }

]


with open(
    "users.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        users,
        file,
        ensure_ascii=False,
        indent=4
    )


print("保存成功")


with open(
    "users.json",
    "r",
    encoding="utf-8"
) as file:

    data = json.load(file)


for user in data:

    print(
        f"用户:{user['name']}"
    )

    print(
        f"资产:{user['money']}元"
    )