"""
函数                                  描述
seed(a=None)                         初始化随机数种子，默认值为当前系统时间
random()                             生成一个[0.0,1.0)之间的随机小数
randint(a, b)                        生成一个[a,b]之间的整数
getrandbits(k)                       生成一个k比特长度的随机整数
randrange(start, stop[, step])       生成一个[start, stop)之间以step为步数的随机整数
uniform(a, b)                        生成一个[a,b]之间的随机小数
choice(seq)                          从序列类型(例如:列表)中随机返回一个元素
shuffle(seq)                         将序列类型中元素随机排列，返回打乱后的序列
sample(pop, k)                       从pop类型中随机选取k个元素，以列表类型返回
"""
## random.seed()
import random

# 设置了seed，那最后的随机数就是固定的
random.seed(1)
print(random.random())

## random()
import random

print(random.random())

## randint()

import random
# 生成1到200之间的随机整数
n = random.randint(1, 200)
print(n)

## getrandbits()
import random

n = random.getrandbits(4)
print(n)

## randrange()
import random

n = random.randrange(1, 10, 2)
print(n)

## uniform(a, b),生成a 到 b 之间的随机小数
import random

n = random.uniform(1, 3)
print(n)

## choice(seq)
import random

n = random.choice(["赵六", "王五", "李四", "张三"])
print(n)

## shuffle(seq)
import random
ls = ["赵六", "王五", "李四", "张三"]
random.shuffle(ls)
print(ls)

## sample(pop, k)
import random
ls = ["赵六", "王五", "李四", "张三"]
n = random.sample(ls, 3)
print(n)