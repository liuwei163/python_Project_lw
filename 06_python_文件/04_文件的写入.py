"""
方法
f.write(s)                  向文件写入一个字符串或字节流
f.writelines(lines)         将一个元素为 字符串 的列表写入文件
"""


# 写入字符串
f = open("C:/Users/Administrator/PycharmProjects/python_Project_lw/06_python_文件/cs1.txt", "w")
n = f.write("学习使人快乐")
print(n)         # 返回写入的字符的个数
f.close()

# f.writelines(lines)         将一个元素为 字符串 的列表写入文件
f = open("C:/Users/Administrator/PycharmProjects/python_Project_lw/06_python_文件/cs1.txt", "w")
ls = str(["liuwei", 1, 3, "刘伟", "aaa"])
f.writelines(ls)
f.close()