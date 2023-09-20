# 计科1914 0306224401 惠骁

def show(lis):
    for i in lis:
        if isinstance(i, list):
            show(i)
        else:
            print(i)


if __name__ == '__main__':
    lis = [1, '小明', '3', [3, '小组']]
    show(lis)
