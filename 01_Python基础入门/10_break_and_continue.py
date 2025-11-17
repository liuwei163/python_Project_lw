# 1. # break 打断当前一层的循环
# 跳出最内层循环，终止该循环后，从循环后的代码继续执行。

# while

# c = 1
# while c <= 10:
#
#     while True:
#         content = input("请输入你要说的话(Q:quit):")
#         if content == 'Q':
#             # c = 100  # 想要打断多层循环，去改变上一层的循环条件
#             break  # 打断当前 while True一层的循环
#         print(content)
#     c = c + 1
# print(c)

c = 1
while c <= 10:
    content = input("请输入你要说的话(Q:quit):")
    if content == 'Q':
        break  # 直接跳出外层循环
    print(content)
    c = c + 1
# for
for i in range(1, 6):
    if i == 3:
        print("这个鸡腿有毒！")
        break
    print("第{}个鸡腿真香".format(i))

# 2.  # continue 停止当前本次的while循环
# 用来结束当前当次循环，即跳出循环体中下面未执行的语句，但不跳出当前循环。

# 通常使用于日志检索

c = 1
while c <= 100:
    #  过滤掉17的倍数
    if c % 17 == 0:   # 17的倍数即条件成立
        c = c + 1     # 将条件c的值加一，否则下次循环c的值依旧是17的倍数
        continue  # 当if条件成立后跳过本次下面的while循环
    c = c + 1
    print(c)

# for
for i in range(1, 6):
    if i == 3:
        print("这个鸡腿太棒了！")
        continue
    print("第{}个鸡腿真香".format(i))

