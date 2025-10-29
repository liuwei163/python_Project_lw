"""
函数                  描述

len(x)               返回字符串x的长度或者是其他组合类型的元素个数(列表)
    chr(x)               返回Unicode编码对应的单字符
    ord(x)               返回单个字符对应的Unicode编码
bin(x)               返回整数x对应的二进制的小写形式
oct(x)               返回整数x对应的八进制的小写形式
hex(x)               返回整数x对应的十六进制的小写形式
str(x)               将x转换为字符串
int(x)               将x转换为整数
float(x)             将x转换为浮点数
type(x)              输出变量x或值的数据类型
"""

# len(x)
# 输出字符串的长度（字符串中的空格也算一个长度）
"""
s = "白色，黑色，蓝色，红色，绿色，青色  2"
print(len(s))
# 输出列表中的元素个数
s1 = ["刘伟", "666", "白色"]
print(len(s1))
"""

# chr(x)
# 返回Unicode编码对应的单字符
"""
print(chr(97))
"""

# ord(x)
# 返回单个字符对应的Unicode编码
# 单个字符需使用引号，引起来
"""
print(ord('a'))
print(ord('b'))
"""

# bin(x)，oct(x)，hex(x)
"""
print(bin(1010))  # 二进制
print(oct(1010))  # 八进制
print(hex(1010))  # 十六进制
"""

# str(x),int(x),float(x)
# type(x) 函数是输出变量x或值的数据类型
"""
print(type(str(1)))
print(type(int("100")))
print(type(float(100)))

# int(x)将浮点数转换为整数，会省略掉小数点后面的内容
print(int(31.44))

# float(x)
    # inx(x),不能转换字符串中的浮点数
    print(int("10.2"))
    # 但是float(x),可以转换字符串中的浮点数为浮点数
    print(float("10.2"))
"""
