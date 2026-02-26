# ls = ['北京', '上海', '重庆']
# f = open('city.csv', "w")
# f. write(','.join(ls) + '\n')
# f.close()

f = open('city.csv', 'r')
# 将文件直接输出，默认为 字符串 (读取一次后，下一次读取就是空)
ls1 = f.read()
# 将文件以列表的形式输出       (读取一次后，下一次读取就是空)
ls = f.read().strip('\n').split(',')
print(ls)
print(ls1)
f.close()
