# print(b // a)  整除
# print(b % a)   获取余数0

a = 13
b = 14
print(a % b)  # 算余数的时候,如果a比b小那么结果一定是为a的

"""
一、 运算符
    1.算数运算
        + - * / // %
        
    2.比较运算
        < > >= <= == !=
        is     # 判断是否是同一个对象,(一般用来判断是否为空None)
        not is # 
"""
# 判空操作
a = None
print(a == None)  # 不建议这样使用
print(a is None)  # 判断变量a是空     (返回True)
print(a is not None)  # 判断变量a不是空 (返回false)

# 赋值运算:
# a = b
# a = a + 1  "和"  a += 1  是一样的效果
# a += b   "和"  a = a + b 是一样的

""" and和or 的逻辑
如果遇到不同的运算符组合.需要注意,计算优先级顺序如下：
() => not => and => or
# print(1 > 2 and 2 > 4 or 3 < 6 or 4 < 7 and 5 > 8)   # 结果 T
# print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6) # 结果 F
        # 0可以表示假
        print(0 and 2)  # 结果为0
        # 非0 可以表示真.
        print(32 and 4) # 结果为4
        # and 的逻辑是:前面这个数字如果有结果了,就得到前面的数字,如果得不到,结果就是后面的数字
        # or 的逻辑和and是相反的
        print(10 or 20) # 结果为10
"""
