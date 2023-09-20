# 计科1914 0306224401 惠骁

list = ["张三", "李四", "王五", "马六", "吴七"]

print("输入名字")
str = input()

# O(n+1)
for i in range(len(list)):
    if str == list[i]:
        print(f"存在捏，位置为：{i}")
        break
else:
    print("不存在捏")

# O(2n)
print(f"存在捏，位置为：{list.index(str)+1}" if list.count(str) > 0 else "不存在捏")
# O(2n)
print(f"存在捏，位置为：{list.index(str)+1}" if str in list else "不存在捏")
