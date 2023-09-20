address_dict = {"小明": "122334455", "小黄": "122334455",
                "小刚": "122334455", "小李": "122334455",
                "小王": "122334455", "小宋": "122334455", }


def home():
    print("欢迎使用个人通讯录系统")
    print("1：查询联系人")
    print("2：插入/更新联系人")
    print("3：删除已有联系人")
    print("4：输出所有联系人信息")
    print("5：退出")


def query():
    name = input("请输入联系姓名")
    print(address_dict.get(name) if name in address_dict else "您输入的姓名不在通讯录中！")


def add():
    name = input("请输入联系人姓名")
    phone = input("请输入用户联系电话")
    address_dict[name] = phone


def deleteAll():
    name = input("请输入联系人姓名")
    address_dict.pop(name)


def show():
    for key, value in address_dict.items():
        print(f"{key}\t{value}")


if __name__ == '__main__':
    home()
    while 1:
        try:
            number = int(input("请输入指令"))
        except Exception:
            print("请输入数字")

            # 3.10新特性
            # match i:
            #     case 1:
            #         query()
            #     case 2:
            #         add()
            #     case 3:
            #         deleteAll()
            #     case 4:
            #         show()
            #     case 5:
            #         break
            #     case _:
            #         print("请输入正确数字")

            # 旧版本
        if number == 1:
            query()
        elif number == 2:
               add()
        elif number == 3:
            deleteAll()
        elif number == 4:
            show()
        elif number == 5:
                # break
            exit()
        else:
            print("请输入正确的数字")
