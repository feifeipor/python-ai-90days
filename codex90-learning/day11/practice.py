import json

user = {"name":"飞飞","age":30,"money":50000}

with (open("baby.json","w",encoding="utf-8") as file):
    json.dump(
        user,
        file,
        ensure_ascii=False,
        indent=4
    )

with open("baby.json","r",encoding="utf-8") as file:

    data = json.load(file)

print(data)