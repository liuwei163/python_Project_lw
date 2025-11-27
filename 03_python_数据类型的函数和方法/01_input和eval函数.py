# input 函数
# 使用方式:<变量> = input(<提示性文字>)
# 将用户输入的内容作为值赋予前面的 变量
# 无论用户输入的是字符还是数字，input()函数统一按照字符类型输出，
s = input("请输入数字：")
print(s)
print(type(s))  # 查看的结果为 str 类型


# eval 函数
# 使用方式:<变量> = eval(<字符串>)
# 去掉字符串最外侧的引号，并按照 Python语句 方式执行去掉引号后的字符内容(变为int类型)
a = input("请输入姓名：")
n = eval(a)     # 如果a的值为字符串类型，则报错。
print(a)
print(type(n))  # 查看的结果为 int 类型
