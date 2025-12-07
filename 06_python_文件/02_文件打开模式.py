"""
    打开模式                        含义
    r                           只读模式，如果文件不存在，返回异常FileNotFoundError，默认值
    w                           覆盖写模式，文件不存在则创建，存在则完全覆盖源文件
    x                           创建写模式，文件不存在则创建，存在则返回异常FileExistsError
    a                           追加写模式，文件不存在则创建，存在则在原文件最后追加内容
    b                           二进制文件模式
    t                           文本文件模式，默认值
    +                           与r/w/x/a一同使用，在原功能基础上增加同时读写功能
                                 r+ 不会清空原来的内容，  w+ 会情况原内容
"""

# w 写入并覆盖源内容，如没有要写入的文件，则创建
f = open("C:/Users/Administrator/PycharmProjects/python_Project_lw/06_python_文件/cs1.txt", "w")
f.write("刘伟")   # 写入
f.close()        # 关闭文件，则保存内容

# x 创建写模式，文件不存在则创建，存在则返回异常FileExistsError
f = open("C:/Users/Administrator/PycharmProjects/python_Project_lw/06_python_文件/cs2.txt", "x")
f.write("刘伟2")   # 写入
f.close()         # 关闭文件，则保存内容

# b 二进制读取文件
f = open("C:/Users/Administrator/PycharmProjects/python_Project_lw/06_python_文件/cs1.txt", "rb")
s = f.read()
print(s)
f.close()

# r+ 不覆盖原来的文件内容以及编码格式/ w+ 相反
f = open("C:/Users/Administrator/PycharmProjects/python_Project_lw/06_python_文件/cs1.txt", "r+")
s1 = f.read()
f.write("123.com222")
print(s1)
f.close()