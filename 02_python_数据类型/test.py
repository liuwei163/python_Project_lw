s = "python"
# 字符串的一个字符是一个序号，

s = (1, 2, 3)
# 元组也可以转换成列表

lt = list(s)
# 列表里的元素之间以逗号分隔，支持双向索引，支持切片
print(lt)

ls = [2, "python", [2, 4, 6], "liuweishishabi"]
print(ls[3])
print(ls[1:3])
print(ls[-3:-1])
print(ls[-2:-4:-1])  # 步长的方向必须与  起始到终止  的方向一致，否则输出为空列表


s = "jhjkh"
s1 = "4542"
print(s+s1)
print(s * 2)


