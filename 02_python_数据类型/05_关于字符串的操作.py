# # 猜数字游戏
# import random  # 用来产生随机数
# n = random.randint(1, 100)  # 随机整数
#
# while 1:
#
#     r = input("请猜测随机数是多少：")
#     if not r.isdigit():  # 判断输入是否为数字，如果输入不是数字则打印一下内容
#         print("请输入0-100的数字")
#         continue  # 停止当前本次循环
#     r = int(r)
#     if r > n:
#         print("猜大了")
#     elif r < n:
#         print("猜小了")
#     else:
#         print("猜对了")
#         break  # 打断当前一层的while循环，（猜对了，退出循环）

# s1 = '张' + '3'
# s2 = '3' + '张'
# s3 = '张' + str(3)
# print(s1, s2, s3)

s = '{0:<10}{1:>5}'.format('x','y')
print(s)
print('acd'.isalpha())