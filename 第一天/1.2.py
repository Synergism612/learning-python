try:
    x = float(input("第一个数字x："))
    y = float(input("第一个数字x："))
    print(f'结果是：{(x+y)}')

except ValueError:
    print('请输入数字!')
