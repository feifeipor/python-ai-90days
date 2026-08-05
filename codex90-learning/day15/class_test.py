class User:

    def __init__(self,name,age):

        self.name = name

        self.age = age


    def show_info(self):
        print(
            f"姓名:{self.name}"
         )

        print(
            f"年龄:{self.age}"
        )

user1 = User(
    "飞飞",
    30
)

user1.show_info()