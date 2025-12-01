# 返回值(将函数内部的 “值” 返回到函数外部)

"""
return语句用来结束函数并将程序返回到函数被调用的位置继续执行。
return语句可以出现在函数中的任何部分
return可以同时返回0个或多个区数运算的结果给函数被调用处的变量。
当return返回多个值时，返回的值形成元组数据类型。
函数也可以没有return代表无返回值。
"""

# 1.返回单个值
def add(x, y):
    s = x + y
    print(s)
    return s  # 将修改后的变量结果返回到调用函数的位置


n = add(1, 9)
print(n)

# 2.返回多个值，（返回的值形成元组的数据类型）
def add(x, y):
    s = x + y
    m = x * y
    print(s)
    return s, y  # 返回多个值


n = add(1, 9)
print(n)    # (10, 9)


# 3.return 也可以用来结束函数的执行
"""
def add(x, y):
    return 0  # 结束函数，下面的代码不执行，直接回到调用函数的位置
    s = x + y
    m = x * y
    print(s)
    return s, m

n = add(1, 9)
print(n)    # 0
"""


def add(x, y):
    if x > y:
        s = x + y
        return s
    else:
        m = x * y
        return m


n = add(10, 9)
print(n)    # 0

# 4.当没有返回值的时候，默认返回的时None（一般不需要去接收这个内容）
def add(x, y):
    s = x + y


n = add(1, 9)
print(n)    # None