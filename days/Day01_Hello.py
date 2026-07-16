#b=10
#print(a)
#name=input("请输入姓名：")
#print(agemixtep)
#print('fefei\\t')#
#print(r'feifei\\t')
#name=input('请输出你的名字')
#if name=="黄振富":
#if name=='冯鸡':
#print('死偶仔')
#hav_money=int(input("身上带了多少钱"))
#hav_time=input('有时间嘛')
#if hav_money>=100:
   # print('今晚吃顿好的！')
   # if hav_time=="有":
    #    print('今晚吃潮发！')
   # elif hav_time=="没":
     #   print('回家睡觉吧')
#elif 100>hav_money>=50:
    ##print('今晚随便吃点')
   # if hav_time=="有":
    #    print("吃个猪脚饭吧")
    #elif hav_time=="没":
       # print('回家睡觉吧')
#elif 50>hav_money>=0:
    #print('挺难搞喔')
    #if hav_time=="有":
       # print('楼下买个泡面吃')
    #elif hav_time=="没":
        #print('回家睡觉咯')
#else :
    #print('难搞了兄弟')
#i=1
#s=0
#while i<=100:
 #   s+=i
 #   i+=1
#print(s)
#i=1
#while i<10:
    #print(f'这是第{i}次外循环')
  #  j=2
  #  while j<10:
  #      print(f'这是第{j}次内循环')
  #      j+=1
  #  i=i+1
#i=1
#s=0
#for i in range(1,101):
 #   s+=i
#print(f'这是第{s}次')
#a='huzai'
#print(a,type(a))
#a1 =a.encode()
#print('编码后:',a1)
#print(type(a1))
#a2 =a1.decode()
#print(a2)
#print('小'+"胡")
#name1="小"
#name2="胡"
#print(name1,name2,sep="")
#na_m="fufnnfinsujeialancckljhcdssncnow,slxk"
#print(na_m[5])
#print(na_m[-5:-15:-2])
#print(na_m.find('a'))
#scro="三十年河东三十年河西，莫欺少年穷"
#print(scro.find('河',5,8))
#print(scro.index('河',5,8))
#print(scro.count('三十',2,10))
#dinner_tonight=['兰州拉面','猪杂粉','螺蛳粉','东北佬']
#while True:
   # di_nn_er=input('吃什么？')
  #  if di_nn_er in dinner_tonight:
  #      print(f'不吃{di_nn_er}可不可以？换一个')
  #  else:
  #      print(f'吃{di_nn_er}')
  #      dinner_tonight.append(di_nn_er)
   #     print(f'就吃这个')
   #     break
# f=open('woshinibaba.txt')
# print(f.name)
# f.close
# a=input('请输入你的体重(公斤):')
# b=input('请输入你的身高(米):')
# Bmi=("a/(a*b)")
# print(Bmi)
# bmi_calculator.py

# def calculate_bmi(weight, height):
#     """计算BMI值，体重kg，身高m"""
#     return weight / (height ** 2)
#
# def get_bmi_category(bmi):
#     """根据BMI值返回分类"""
#     if bmi < 18.5:
#         return "偏瘦"
#     elif 18.5 <= bmi < 25:
#         return "正常"
#     elif 25 <= bmi < 30:
#         return "超重"
#     else:
#         return "肥胖"
#
# def main():
#     print("=== BMI 体重计算器 ===")
#     try:
#         weight = float(input("请输入体重（公斤）："))
#         height = float(input("请输入身高（米）："))
#         if weight <= 0 or height <= 0:
#             print("体重和身高必须为正数！")
#             return
#         bmi = calculate_bmi(weight, height)
#         category = get_bmi_category(bmi)
#         print(f"您的BMI指数为：{bmi:.2f}")
#         print(f"分类：{category}")
#     except ValueError:
#         print("输入无效，请输入数字！")
#
# if __name__ == "__main__":
#     main()