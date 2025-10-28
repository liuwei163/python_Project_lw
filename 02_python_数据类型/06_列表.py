# 列表
    # 主要用来存储大量的数据。
    # python中使用[]表示列表 或者 list() 表示列表
    # 字符串类型也可以存储，但是提取数据不方便。
    # 列表也有索引和切片，提取数据可直接使用索引
    # 列表里存储的数据，没有类型要求，数值和字符串都可以

# 1)列表也有索引，提取数据可直接使用索引
lst = ["192.168.1.1", "192.168.1.2"]

ip = lst[1]
print(ip)

# 切片使用冒号:
lst = ["刘妍", "刘伟", "杨妍", "杨伟"]
print(lst[-3:-1])
print(lst[::-1])
print(lst[::1])
print(lst[-3:-4])  # 步长 (默认是1的情况下,start和end的方向必须为正,否则结果是空列表,如果要负方向取值，则需要使用 负步长)


# 2) 列表是一种可以变化的数据类型：（新增 和 修改）
# 新增数据
lst = []
lst1 = ["李四", "王五"]
# append没有返回值，在列表的末尾追加新内容
lst.append("刘伟")
lst.append("杨妍")

# inster,在指定的位置插入新数据
lst.insert(1, "张三")  # 序号1 位置插入新数据
print(lst)

# extend 是把后面lst1列表合并到lst列表中
lst.extend(lst1)
print(lst)

# 修改数据
lst1 = ["李四", "王五"]
# 将序号0位置修改为张三
lst1[0] = "张三"
print(lst1)

# 删除数据(很少使用)
lst1 = ["李四", "王五"]
lst1.pop(0)  # 给序号删除指定位置的数据
print(lst1)
lst1.pop()   # 不给序号默认删除最好一项数据
print(lst1)

# 查询数据
# 普通查询方式(索引)
lst1 =["张无忌1", "夏侯惇", "张无忌2", "百里守约"]
item = lst1[2]
print(item)

# 循环遍历查询(看不到索引 ！！！) 只是修改没有，把修改后的结果保存回原表中
lst1 =["张无忌1", "夏侯惇", "张无忌2", "百里守约"]
for item in lst1:
    if item[0] == '张':
        item = "王" + item[1:]
print(lst1)
# 通过索引遍历列表
lst1 =["张无忌1", "夏侯惇", "张无忌2", "百里守约", "李张二"]
# range函数
# 让for循环可以进行数数
# range(n)  # 0~n  取不到n，切片逻辑一样，包头不包尾
# len函数是Python的内置函数，用于返回对象的长度（元素个数）。

for i in range(len(lst1)):     # len(lst1) 返回列表长度 5 # range(5) 生成序列 [0, 1, 2, 3, 4]
    item = lst1[i]             # 获取当前索引位置的元素值
    if item.startswith("张"):  # .startswith, 检查字符串是否以"张"开头
        item = "王" + item[1:]
        lst1[i] = item   # 修改列表
print(lst1)

# 使用列表推导式（更Pythonic）
lst1 = ["张无忌1", "夏侯惇", "张无忌2", "百里守约", "李张二"]
lst1 = ["王" + item[1:] if item.startswith("张") else item for item in lst1]
print(lst1)
