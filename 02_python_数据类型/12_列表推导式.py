# Python 列表推导式(list comprehension)是一种简洁快速创建列表的方法。
# 它的结构是在方括号内，包含一个表达式，后面跟一个for子句，
# 然后是零个或多个for或if子句。返回的列表由表达式计算的结果组成。

# ls = []
#
# for i in  range(5):
#     ls.append(i)
# print(i)
# print(ls)

# 将后面for循环后的内容，赋值给前面的变量i ，print输出变量i的值, [i]表示i是一个列表
print([i for i in range(5)])



# if 判断5 大于 3 和小于 3 分别输出什么内容
# if 5 > 3:
#     print(5)
# else:
#     print(3)

# if else 简写
print(5) if 5 > 3 else print(3)

# 创建一个列表，0-5数字， （> 2）的数字把 0 添加到列表，（<=2） 的数字，把原数字添加到列表
# ls = []
# for i in range(5):
#     if i > 2:
#         ls.append(0)
#     else:
#         ls.append(i)
# print(ls)

print([0 if i > 2 else i for i in range(5)])
