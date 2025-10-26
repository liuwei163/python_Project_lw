s = "python是世界上最好的编程语言"

'''
# 索引
    # 索引是从0开始计算的
    print(s[0])
    print(s[6])
    # python的字符串索引是可以从右向左计算的
    print(s[-1])
    print(s[-3])

s = "刘伟666"
print(s[1], s[0]) #先输出伟 再输出刘
'''


""" # 切片

    切片的规则 [start: end]
        从start位置开始取，但是最后的end是取不到的
        print(s[1: 4])  # 得到 yth

        start位置和end位置 如果不写则取最边界的值
        print(s[: 4])   # 取到 pyth
        print(s[2: ])   # 取到 thon是世界上最好的编程语言
        print(s[:])     # 取到 python是世界上最好的编程语言
    
        也可以这样使用
        print(s[-6: -1]) # 取到 好的编程语
        
    切片的规则 [start:end:step]  # step：步长 每几个出来1个
    print(s[::2]) # 取到 pto是界最的程言
    
    step如果是正数（从左到右），如果是负数（从右到左）。
    print(s[-1: -5: -1]) # 取到 言语程编
"""

""" # 切片的使用场景

# 判断一句话是否是回文(从左向右读,从右向左读一样的)

s ="黄山落叶松叶落山黄"

s1 = s[ ::- 1]
if s == s1:
    print("是回文")
else:
    print("不是回文")
"""