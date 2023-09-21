# 计科1914 0306224401 惠骁

import random

# 打开并读取学生原名单文件
with open('D:/data/github/learning-python/第四天/students_old.txt', 'r', encoding='UTF-8') as file_old:
    lines_old = file_old.read().splitlines()

# 从原名单中随机选择一名学生
selected_student = random.choice(lines_old)

# 删除
lines_old.remove(selected_student)

# 将剩余的学生写回原文件
with open('D:/data/github/learning-python/第四天/students_old.txt', 'w', encoding='UTF-8') as f:
    f.writelines(map(lambda x: f"{x}\n", lines_old))

# 追加到新名单
with open('D:/data/github/learning-python/第四天/students_new.txt', 'a', encoding='UTF-8') as file_new:
    file_new.write(f"{selected_student}\n")
