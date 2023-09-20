# 计科1914 0306224401 惠骁

import random

balls = list(range(1, 10))
daizi = [[], [], []]

# 3/3/3随机分配
print(balls)
random.shuffle(balls)

for ball in balls:
    if ball % 3 == 0:
        daizi[0].append(ball)
    if ball % 3 == 1:
        daizi[1].append(ball)
    if ball % 3 == 2:
        daizi[2].append(ball)

print(daizi)

# 不定随机分配
daizi = [[], [], []]

for ball in balls:
    daizi[random.randint(0, 2)].append(ball)
print(daizi)
