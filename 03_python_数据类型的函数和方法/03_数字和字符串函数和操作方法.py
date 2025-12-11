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
# float也可以将字符串中的整数转换为浮点数
"""

#################################################################################
# 操作方法：
"""
# 方法                               描述
str.lower()                        以小写的方式全部返回str的副本
str.upper()                        以大写的方式全部返回str的副本
str.split(sep=None)                返回一个列表，以sep作为分隔点，sep默认为空格或换行
str.count(sub)                     返回sub子串出现的次数
str.replace(old,new)               返回字符串str的副本，所有old子串被替换为new
str.center(width,fillchar)         字符串居中函数，fillchar参数可选
str.strip(chars)                   从字符串str中去掉在其左侧和右侧chars中列出的字符
str.join(iter)                     将iter变量的每一个元素后面（元素和元素中间）增加一个str字符串
"""

# str.lower()
s = "aBcDeFg"
print(s.lower())

# str.upper()
s = "aBcDeFg"
print(s.upper())

# str.split(sep=None)
# 以, 号作为分隔符
s = "北京,上海,天津 重庆"
print(s.split('.'))
print(s.split())   # 默认使用空格为分隔符

# str.count(sub)
s = "abcabcabcababc"
print(s.count('ac'))

# str,replace(old,new)
# 字符串中有几个匹配old的内容，都会被替换成new的内容
s = "北京,上海,天津 重庆 天津天津"
print(s.replace("天津", "山西"))

# str.center(width,fillchar)
s = "666小黑666"
print(s.center(20, "*"))

# str.strip()
s = "67666小黑66676"
print(s.strip("6"))

# str.join(iter)
# 将 s 变量的每一个元素和元素中间加一个 + 号
s = "小黑小白绿蓝红"
print("+".join(s))

#################################################################################
# 方法                                       描述
# str.isalpha()                             检查字符串是否只包含字母字符
# 如果字符串中的所有字符都是字母（a-z, A-Z），返回 True
# 如果字符串包含任何非字母字符（数字、空格、标点等），返回 False
# 对于空字符串，返回 False
print('acd'.isalpha())

