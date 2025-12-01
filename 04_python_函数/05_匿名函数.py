# 匿名函数适合处理临时需要一个类似于函数的功能但又不想定义函数的场合，
# 可以省去函数的定义过程和考虑函数的命名，让代码更加简洁，可读性更好。
"""
表达式如下：


"""
# 正常的定义函数流程
def add(x, y):
    return x + y
n = add(1, 4)
print(n)


# 匿名函数
fun = lambda x, y: x + y
print(fun(2, 5))

# 真正的匿名匿名函数
print((lambda x, y: x + y)(2, 5))