"""
方法
f.read()                        文件中读入整个文件内容。
f.readline()                    从文件中读入一行内容。
f.readlines()                   从文件中读入所有行，以每行为元素形成一个列表。
f.seek(offset,whence)           改变当前文件操作指针的位置，whence的值: 0:文件开头; 1:当前位置 2:文件结尾
    # f.seek(offset,whence)方法能够移动读取指针的位置。
    #  offset:开始的偏移量，也就是代表需要移动偏移的字节数，如果是负数表示从倒数第几位开始往前偏移（需要以rb二进制方式打开）
        偏移的时字节，不是字符
    #  whence:可选，默认值为 0
        # 给offset 定义一个参数，表示要从哪个位置开始偏移;
        # 0代表从文件开头开始算起，1代表从当前位置开始算起，2 代表从文件末尾算起：（需要以rb二进制方式打开）
"""

# readline()  每次只读取文件的一行
f = open("C:/Users/Administrator/PycharmProjects/python_Project_lw/06_python_文件/cs1.txt", "r+")
s1 = f.readline()      # 读取文件的第一行，包括换行符
s2 = f.readline()      # 读取文件的第二行，包括换行符
print(s1)
print(s2)
f.close()

# readlines() 从文件中读入所有行，以每行为元素形成一个列表。
f = open("C:/Users/Administrator/PycharmProjects/python_Project_lw/06_python_文件/cs1.txt", "r+")
s1 = f.readlines()      # 读取文件的第一行，包括换行符
print(s1)
f.close()

# f.seek(offset,whence)         改变当前文件操作指针的位置，whence的值: 0:文件开头; 1:当前位置 2:文件结尾
f = open("C:/Users/Administrator/PycharmProjects/python_Project_lw/06_python_文件/cs1.txt", "r+")
s3 = f.read()
s1 = f.seek(2, 0)
s2 = f.read()
print(s3)
print("########!!!!!!!!!!!!!!!!!")
print(s1)
print("##############################")
print(s2)
f.close()

# 从后往前偏移
f = open("C:/Users/Administrator/PycharmProjects/python_Project_lw/06_python_文件/cs1.txt", "rb")
s3 = f.read()
s1 = f.seek(-2, 2)
s2 = f.read()
print(s3)
print("########!!!!!!!!!!!!!!!!!")
print(s1)
print("##############################")
print(s2)
f.close()
