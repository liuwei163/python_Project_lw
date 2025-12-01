def add(x, y):
    return x + y
n = add(1, 4)
print(n)


# 匿名函数
fun = lambda x, y: x + y
print(fun(2, 5))

# 真正的匿名匿名函数
print((lambda x, y: x + y)(2, 5))