# 简单的if嵌套方式
"""
name = input("姓名:")
if name == "刘伟":

    number = input("你的手机号后四位:")
    if number == "4154":
        print("通过")
    #
    elif number != "4154":
        print("不通过")
else:
    print('不通过')

#### 可以一直进行if嵌套,但不介意进行多层嵌套(可使用逻辑运算符进行条件拼接)
name = input("姓名:")
if name == "刘伟":

    number = input("你的手机号后四位:")
    if number == "4154":
        print("通过")

        youid = "140"
        if youid == "140":
            print("通过")
        else:
            print("不通过")

    else:
        print("不通过")
else:
    print('不通过')
"""

# 逻辑运算符
"""
1. 两个条件或者多个条件需要('同时'或'一个条件') 成立的时候, 可以使用: and 和 or
and: 必须保证左右两端条件同时成立,结果才是 True
    x1 and x2
    如果x1 为假，结局一定是假 x2不再进行判断
or: 两端只要有一个条件成立,结果就会是 True
    x1 or x2
    如果x1 为假，x2正常进行判断
    如果x1 为真，x2不再进行判断
not: 不
    not x
    如果x条件是假，计算结果就是True
    如果x条件是真，计算结果就是False
"""
username = input("请输入用户名:")
password = input("请输入密码:")
if password != (0-9):
    password = int(input("请输入6位数字密码:"))

elif username == "admin" and password == "123456":
    print("登录成功")
else:
    print("登录失败")