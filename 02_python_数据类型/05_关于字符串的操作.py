# # # 猜数字游戏
"""
import random               # 拉取标准库中的模块用来产生随机数
n = random.randint(1, 100)  # randint: 产生随机整数

while 1:

    r = input("请猜测随机数是多少：")
    if not r.isdigit():  # 判断输入是否为数字，如果输入不是数字则打印以下内容
        print("请输入0-100的数字")
        continue  # 停止当前本次循环，开启下一次循环
    r = int(r)
    if r > n:
        print("猜大了")
    elif r < n:
        print("猜小了")
    else:
        print("猜对了")
        break     # 打断当前一层的while循环，（猜对以后，退出循环）
"""
# 1)字符串类型,不可用来"运算",但是可以用来"拼接" 如: a + b =ab
s1 = '张' + '3'
s2 = '3' + '张'
s3 = '张' + str(3)
print(s1, s2, s3)

# 大小写转换
s = "Python"
s3 = s.upper()
print(s3)  # 输出：PYTHON
print(s)   # 输出：Python

# 格式化
s4 = f"Learn {s}"
print(s4)  # 输出：Learn Python

"""
字符串在python中是一个不可变的数据类型
在Python中，字符串的不可变性意味着你永远不能"原地"修改字符串，所有修改操作都会返回新的字符串对象。
# 创建一个字符串
text = "Hello"

# 尝试修改字符串
try:
    text[0] = "h"  # 尝试将第一个字符改为小写
except TypeError as e:
    print(f"错误：{e}")  # 这会抛出 TypeError

# 正确的"修改"方式
text = "Hello"
new_text = text.replace("H", "h")  # 创建了一个新字符串
print(f"原字符串：{text}")      # 输出：Hello
print(f"新字符串：{new_text}")  # 输出：hello
print(f"内存地址是否相同：{id(text) == id(new_text)}")  # 输出：False
"""

# 2)format方法的基本使用
# 字符串使用方式:<模板字符串>.format(<逗号分隔的参数>)
# 其中模板字符串是一个由 字符串 和 槽 组成的字符串，用来控制字符串和变量的显示效果
n = input("请输入鸡腿个数：")
m = input("请输入鸡蛋个数：")
a = "今天中午我吃了{}个鸡腿，{}个鸡蛋".format(n, m)    # {} 大括号就是代表"槽" 默认序号是0~1
b = "今天中午我吃了{1}个鸡腿，{0}个鸡蛋".format(n, m)    # 默认按照顺序传，但是也可以使用序号 让他传到指定位置
print(a)
print(b)
print(type(a))

# format方法格式控制
# format()的槽不仅包括参数序号还包括格式控制信息，语法格式为!
# {参数序号>:<格式控制标记>}



# s = '{0:^10}{1:>5}'.format('x', 'y')
# print(s)
# print('acd'.isalpha())


