# 计科1914 0306224401 惠骁

class Cat:
    def __init__(self, name, titi):
        self.name = name
        self.tili = titi

    def play(self):
        self.tili -= 1
        print(f"{self.name}在玩耍，体力减少了1点，现在体力为{self.tili}点。")

    def sleep(self):
        self.tili += 5
        print(f"{self.name}在睡觉，体力补充了5点，现在体力为{self.tili}点。")

# 创建猫类的对象cat1
cat1 = Cat("小花", 10)

# 调用玩耍和睡觉方法
cat1.play()
cat1.sleep()