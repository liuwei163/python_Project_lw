# 打开文件
## 2.使用绝对路径的方式打开（输入文件的完整路径）
# 将反斜杠替换为斜杠，使用python中的路径格式（方式3）
f = open("C:/Users/Administrator/PycharmProjects/python_Project_lw/06_python_文件/cs1.txt", "rb")
# 操作文件，读取
s = f.read()
print(s)
# 关闭文件
f.close()
