try:
    # n = eval(input("请输入一个数字："))
    # print(n ** 5)
    print(2/1)
# except NameError:
#     print("请输入数字，不要输入其他内容！")
except ZeroDivisionError:
    print("除零错误！！！")
finally:
    print("不管是否正常，都会执行。")