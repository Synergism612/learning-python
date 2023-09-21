# 计科1914 0306224401 惠骁

import re

pwd = input("请输入密码")
pattern = r'^[a-zA-Z0-9]+$'

# 中文存在问题
# if pwd.isalnum():
if re.match(pattern, pwd):
    if len(pwd) <= 8 or pwd.isdigit() or pwd.isalpha():
        print("简单密码，合格")
    elif len(pwd) > 8:
        print("复杂密码，合格")
else:
    print("存在特殊字符")
