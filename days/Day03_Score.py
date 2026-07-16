# wather='下雨'
# if wather =="下雨":
#     print('记得带伞')
# weather = input("今天天气：")
# if weather == "下雨":
#     print("带伞")
# else:
#     print("戴墨镜")
#==========智能成绩分析器===========
while True:
    name=input('请输入你的姓名：')
    Ace=float(input('请输入你的成绩；'))
    if 0<=Ace<=100:
        if Ace <= 100 and Ace >= 90:
            print("优秀")
        elif Ace <= 89 and Ace >= 80:
            print('良好')
        elif Ace <= 79 and Ace >= 60:
            print('及格')
        else:
            print("不及格")
        break
    else:
        print("成绩输入错误，请重新输入姓名和0～100 之间的数字。")



