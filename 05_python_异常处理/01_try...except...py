"""
try:
    <语句块1>  # 可能会发生异常的代码，先执行一下试试
except <异常类型>:   # 为空的时候表示捕获所有错误类型
    <语句块2>  # 如果try中代码抛出异常并被except捕获，执行此处代码

else:
    <语句块3> # try代码正常执行，则执行此处代码
"""
try:
    n = eval(input("请输入一个数字："))
    print(n ** 5)
except:    # 为空的时候表示捕获所有错误类型
    print("请输入数字，不要输入其他内容！")
else:
    print("程序没有发生异常。")
"""
try:
    <语句块1>  # 可能会发生异常的代码，先执行一下试试
except <异常类型>:
    <语句块2>  # 如果try中代码抛出异常并被except捕获，执行此处代码

finally:
    <语句块3> # 不管有没有问题都会执行
"""
try:
    n = eval(input("请输入一个数字："))
    print(n ** 5)
except:
    print("请输入数字，不要输入其他内容！")
finally:
    print("不管是否正常，都会执行。")

# 多种异常类型
try:
    # n = eval(input("请输入一个数字："))
    # print(n ** 5)
    print(1/0)
# except NameError:               # 捕捉非零的输入
#     print("请输入数字，不要输入其他内容！")
except ZeroDivisionError:         # 捕捉除零错误
    print("除零错误！！！")
finally:
    print("不管是否正常，都会执行。")