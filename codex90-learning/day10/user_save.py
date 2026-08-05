name = "飞飞"

age = 30

job = "咖啡师"


with open(
    "user.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(
        name + "\n"
    )

    file.write(
        str(age) + "\n"
    )

    file.write(
        job
    )