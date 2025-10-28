# range函数 (和切片的逻辑几户一样)
"""
    range()
    让for循环可以进行数数
    range(n)         0~n
    range(m, n)      m~n
    range(m, n, p)   m~n每p个出来1个
"""
lst1 =["张无忌1", "夏侯惇", "张无忌2", "百里守约", "李张二"]
for i in range(len(lst1)):      # len(lst1) 返回列表长度 5 # range(5) 生成序列 [0, 1, 2, 3, 4]
    item = lst1[i]              # 获取当前索引位置的元素值
    if item.startswith("张"):   # .startswith, 检查字符串是否以"张"开头
        item = "王" + item[1:]
        lst1[i] = item   # 修改列表
print(lst1)

# len函数是Python的内置函数，用于返回对象的长度（元素个数）

