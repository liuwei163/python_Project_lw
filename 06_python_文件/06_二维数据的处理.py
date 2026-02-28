# 1、二维数据由一维数据组成，用CSV格式文件存储。CSV文件的每一行是一维数据，整个CSV文件是 一个二维数据。
# 2、二维列表对象输出为CSV格式文件方法如下，采用遍历循环和字符串的 join()方法相结合

# 二维数据的存储
"""
ls = [['学校', '报考人数', '往年录取人数', '理科人数'],
      ['xx实验中学', '100', '60', '60'],
      ['xx中学', '150', '30', '80'],
      ['xx高级中学', '200', '140', '160']
      ]

f = open('school.csv', 'w')

for i in range(len(ls)):
    f.write(','.join(ls[i]) + '\n')

f.close()
"""
# 二维数据的读取
"""
L = []
f = open('school.csv', 'r')

ls = f.readlines()
print(ls)

# s = f.read()
# ls = s.strip('\n').split('\n')
for i in ls:
    lt = i.strip('\n').split(',')
    L.append(lt)
print(L)
f.close()
"""
# 二维数据的格式化输出，打印成表格
L = []
f = open('school.csv', 'r')
for i in f:
    lt = i.strip('\n').split(',')
    L.append(lt)

for row in L:
    for col in row:
        print(col, end='\t')
    print()

f.close()
