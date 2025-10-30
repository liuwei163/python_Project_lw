# 方法                               描述
# str.lower()                        以小写的方式全部返回str的副本
# str.upper()                        以大写的方式全部返回str的副本
# str.split(sep=None)                返回一个列表，以sep作为分隔点，sep默认为空格或换行
# str.count(sub)                     返回sub子串出现的次数
# str.replace(old,new)               返回字符串str的副本，所有old子串被替换为new
# str.center(width,fillchar)         字符串居中函数，fillchar参数可选
# str.strip(chars)                   从字符串str中去掉在其左侧和右侧chars中列出的字符
# str.join(iter)                     将iter变量的每一个元素后面（元素和元素中间）增加一个str字符串

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

