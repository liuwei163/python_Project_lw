#  将 input 获取到的值转换为int类型 赋值给变量money
# money = int(input("请输入钱数:"))

# 1.当条件成立时，执行下面的内容
# if money > 500:
#     #  前面有一个缩进。表示当前代码从属于if语句
#     print("happy一下")
#     print("大吃大喝一顿.")
# #  没有缩进的。就和if没关系了正常运行
# print("回家..")

#  2.当条件不成立时，执行else下面的内容，然后正常往下执行
# money = int(input("请输入你兜里的钱:"))
# if money > 500:
#     print("happy 一下")
# else:
#     print("去搬砖....")
#
# print("回家")

#  3.当条件1不成立时，判断条件2是否成立，条件2不成立时判断条件3是否成立
#  当其中一个条件成立后执行elif下面的内容，然后跳过此if语句中的其它判断条件，正常执行if语句外的代码
money = int(input("请输入你兜里的钱:"))
if money > 5000:
    pass  # 当不确定条件成立应该干什么的时候，可以先使用pass保证程序结构完整
    #  print("happy ten")
elif money > 1000:
    print("heppy two")
elif money > 200:
    print("heppy one")
else:
    print("去搬砖....")

print("回家")