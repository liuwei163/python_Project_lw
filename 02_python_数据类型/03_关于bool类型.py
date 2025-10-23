# a = 18
# # 想得到结果"18哈哈"
# a = str(a) # 强制类型转换
# print(a +"哈哈")

a = 18
print(bool(a))  # True
print(bool(0))  # False
print(bool(-1))  # True

# 小结论，所有的数字：非零的表示为真，零表示为假

# 0-> 没有东西 -> False
print(bool("字符串"))  # True
print(bool(""))       # False
print(bool(" "))      # 空格也为真True
# 小结论,所有的字符串,空的字符串就是假,非空字符串结果是真

print(bool([11, 22, 33]))  # True
print(bool([]))    # False
print(bool([""]))  # True
# 小结论,列表,里面如果有东西,结果是真,没东西,结果是假#

## 总结，所有可以表示"空"的东西结果为假的，反之则为真


# None,空,真空. 什么操作都没有.

# print(bool(None))  # False

# python中表示假的东西:
# 0, "", [], (), {}, set(), b'', None

# 可以和if或者while结合使用
while 1:
    print("你好啊,")


info = []  # 这里是采集到的服务器数据
if info:
    print("采集到了")
else:
    print("没采集到")

if not info:
    print("没采集到")
