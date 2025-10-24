#1. # python3.6之前
"""
name = "刘伟"
age = 18

# %s :占位 s表示往里面放字符串
# %d :占位 d表示往里面放数字(数字也可以当字符串)

s = "我叫%s,我今年%d岁" % (name, age)
print(s)
"""


#2. # python3.6之后，推荐使用f-string来进行数据的格式化输出
"""
语法：
f-string:
    f"xxx{变量}xxxxx{表达式}xxxx"
"""
name = "刘伟"
age = 18
        # 表达式中可以进行运算
s = f"我叫{name},我今年{age+1}岁"
print(s)
