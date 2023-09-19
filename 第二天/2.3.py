import random

x = random.randint(1, 100)
print("猜猜看啊")

try:
    z = 0
    while 1:
        if z == 5:
            print(f"你输了，答案是{x}")
        y = int(input())
        if y == x:
            break
        elif y < x:
            print("比这个大")
        else:
            print("比这个小")
        z += 1
    print("棒！你猜对了！")
except:
    print("输入整数")
