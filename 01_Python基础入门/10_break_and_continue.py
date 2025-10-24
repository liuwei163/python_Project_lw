#1. # break 打断当前一层的循环

# c = 1
# while c <= 10:
#
#     while True:
#         content = input("请输入你要说的话(Q:quit):")
#         if content == 'Q':
#             c = 100  # 想要打断多层循环，去改变上一层的循环条件
#             break  # 打断当前 while True一层的循环
#         print(content)
#     c = c + 1


#2.  # continue 停止当前本次的while循环
# 通常使用于日志检索

c = 1
while c <= 100:
    #  过滤掉17的倍数
    if c % 17 == 0:   # 17的倍数即条件成立
        c = c + 1     # 将条件c的值加一，否则下次循环c的值依旧是17的倍数
        continue  # 当if条件成立后跳过本次while循环
    c = c + 1
    print(c)


