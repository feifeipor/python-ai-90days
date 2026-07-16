from tools import add, subtract, multiply, future_money
#从 tools 这个工具包里面的 calculator 模块，拿 add 这个函数出来。
print(add(10,5))
print(subtract(10,5))
print(multiply(10,5))

money = future_money(10000,5000,10,0.08)
print(f'未来资产: {money:.0f}元')