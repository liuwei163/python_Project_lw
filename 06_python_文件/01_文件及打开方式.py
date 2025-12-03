"""
    2、Python通过open()函数打开一个文件，并返回一 个操作这个文件的变量
    语法形式如下:
        <变量名> = open(<文件路径及文件名>, <打开模式>, <编码格式>)

    打开模式                        含义
    r                           只读模式，如果文件不存在，返回异常FileNotFoundError，默认值
    w                           覆盖写模式，文件不存在则创建，存在则完全覆盖源文件
    x                           创建写模式，文件不存在则创建，存在则返回异常FileExistsError
    a                           追加写模式，文件不存在则创建，存在则在原文件最后追加内容
    b                           二进制文件模式
    t                           文本文件模式，默认值
    +                           与r/w/x/a一同使用，在原功能基础上增加同时读写功能

"""

# 打开文件
## 1.使用相对路径的方式打开（要打开的文件和脚本在同一个目录中）
# r 表示只读模式打开，t 表示以文本文件模式打开（默认值）
f = open("cs1.txt", "rt", encoding='utf-8')
# 操作文件，读取
s = f.read()
print(s)
# 关闭文件
f.close()

## 2.使用绝对路径的方式打开（输入文件的完整路径）（有三种方式）

# 使用反斜杠将后面的反斜杠转义为普通字符（方式1）
f = open("C:\\Users\\Administrator\\PycharmProjects\\python_Project_lw\\06_python_文件\\cs1.txt", "r", encoding='utf-8')
# 在路径前加上 r 表示将后面的内容全部取消字符的特殊含义（方式2）
f = open(r"C:\Users\Administrator\PycharmProjects\python_Project_lw\06_python_文件\cs1.txt", "r", encoding='utf-8')
# 将反斜杠替换为斜杠，使用python中的路径格式（方式3）
f = open("C:/Users/Administrator/PycharmProjects/python_Project_lw/06_python_文件/cs1.txt", "r", encoding='utf-8')

# 操作文件，读取
s = f.read()
print(s)
# 关闭文件
f.close()