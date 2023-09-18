try:
    x = int(input("第一个数字x："))
    y = int(input("第一个数字x："))
    z = int(input("第一个数字x："))
    print(f'结果是：{(x+y+z)}')

except ValueError:
    print('请输入数字!')
