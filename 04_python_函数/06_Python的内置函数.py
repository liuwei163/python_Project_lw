# all后全部为真（非0非空即为真）：返回True，反之则返回False
all([1,3,4,5,6])
True
all([1,3,4,5,6,0])
False

# any只要有一个为真，即判断为True
any([1,3,5,6,7,0])
True
any([1,0,0])
True

# eval去掉双引号并执行(默认：双引号中内容为字符串)
eval("1+2")
3

# exec默认没有返回值，默认为None
exec("1+2")

exec("a = 1+2")
print(a)
3

# sorted对列表中的内容进行排序
sorted([1,5,2,6,8,4,3])
[1, 2, 3, 4, 5, 6, 8]
# sorted,使用reverse参数，是否反转
sorted([1,5,2,6,8,4,3],reverse=True)
[8, 6, 5, 4, 3, 2, 1]

# sum求和
sum([1,4,5,8])
18

# reversed()函数使用：
reversed([1, 2, 3, 4, 5, 6])
< list_reverseiterator object at 0x0000013640B4B940 >
# 通过打印变量i 来查看reversed()函数排序
for i in reversed([1, 2, 3, 4, 5, 6]):
    print(i)

6
5
4
3
2
1