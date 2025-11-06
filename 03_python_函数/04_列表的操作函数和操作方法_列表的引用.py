# 操作函数          描述
# len(ls)         列表ls的元素个数(长度)
# min(ls)         列表ls中的最小元素(内部数据可比较)
# max(ls)         列表ls中的最大元素 (内部数据可比较)
# list(x)         将x转变成列表类型

# 列表中len函数 用来统计列表中的元素个数(长度)
ls = ["刘伟", 20, "张三", 30, "李四", 50]
print(len(ls))

# min和max
lt = [2, 4, 3, 6, 1, 20]
print(min(lt))   # 列表中最小的
print(max(lt))   # 列表中最大的

# list(x)
# 可以将x(如：字符串类型，集合类型，元组类型)转换成列表类型
ls = list("python123")
print(ls)

###############################################################################
# 操作方法，语法形式是：
# <列表变量>.〈方法名称>(<方法参数>)
"""
方法                                             描述
ls.append(x)                                    在列表ls最后增加-个元素x
ls.insert(index,x)                              在列表ls第index位置增加元素x
ls.clear()                                      删除ls中所有元素
ls.pop(index)                                   将列表ls中第index项元素取出并删除该元素
ls.remove(x)                                    将列表中出现的第一个元素x删除
ls.reverse()                                    列表ls中元素反转
ls.copy()                                       生成一个新列表，复制ls中所有元素
"""

# ls.append(x) 列表最后添加一个元素x
ls = ["刘伟", 20, "张三", 30, "李四"]
ls.append("小白")
print(ls)

# ls.insert(index,x) 在列表ls的第index位置增加一个元素x
# index  使用索引来定位
ls.insert(1, "小粉")
print(ls)

# ls.clear() 清空列表中的元素
    # ls.clear(ls)
    # print(ls)

# ls.pop(index) 将列表ls中第index项元素取出并删除该元素
print(ls.pop(1))  # 删除小粉,print函数输出删除的具体元素
print(ls)         # 没有小粉了

# ls.remove(x) 将列表中出现的第一个元素x删除
ls.remove("刘伟")  # 删除指定的元素
print(ls)

# ls.reverse() 列表ls中元素反转
ls.reverse()
print(ls)         # ['小白', '李四', 30, '张三', 20]

# ls.copy() 生成一个新列表，复制ls中所有元素
new_ls = ls.copy()   # 赋值给一个新的变量名
print(new_ls)


#################################################################################
# 对于基本的数据类型，如整数或字符串，可以通过等号实现元素赋值。
# 但对于列表类型，使用等号无法实现真正的赋值。
# 其中，ls = lt语句并不是拷贝lt中元素给变量ls，而是新关联了一个引用，即ls和lt 所指向的是同一套内容。

# 分别给a和b赋值
a, b = 1, 2
a = b      # 将b的值 赋值给a
print(a)   # 输出为b的值

# 列表的引用
ls = ["100", "李伟", "python"]
lt = ls      # 并不是将ls赋值给lt，而是lt列表引用了ls列表的内容
print(lt)
ls.clear()   # 只清空了ls列表，但是因为lt引用的是ls列表的内容，所以lt列表也为空
print(lt)    # 空列表

# 要想修改ls列表不影响lt列表的内容，则需要使用ls.copy()方法，将ls列表复制以后赋值给lt列表
ls = ["100", "李伟", "python"]
lt = ls.copy()
ls.clear()
print(lt)






