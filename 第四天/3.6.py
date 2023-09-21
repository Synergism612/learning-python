# 计科1914 0306224401 惠骁

import random

def random_pick(n):
    balls = ['红球', '黄球', '绿球'] * (n // 3 + 1) + ['红球', '黄球', '绿球'][:n % 3]
    return random.sample(balls, n)

n = int(input("请输入你想随机选几次（每次至少选一个）："))
for _ in range(n):
    print(random_pick(8))
