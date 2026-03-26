"""
处理时间是程序最常用的功能之一，
time库是Python提供的处理时间标准库。
time库提供系统级精确计时器的计时功能，可以用来分析程序性能，也可让程序暂停运行时间。
"""

"""
time库的功能主要分为3个方面:
    时间处理、时间格式化和计时。·
时间处理主要包括4个函数:
    time.time()、time.gmtime()、time.localtime()、time.ctime().
时间格式化主要包括3个函数:
    time.mktime()、time.strftime()、time.strptime().
·计时主要包含用到1个函数:
    time.sleep()
"""

import time
print(time.time())

# 获取UTC时区的时间
print(time.gmtime())

# 获取本地的时区时间，国内为北京时间
print(time.localtime())

# 格式化输出（国外格式）
print(time.ctime())
# 输出结果：Thu Mar 26 16:11:02 2026

# 格式化输出函数
import time
t = time.localtime()

# mktime将localtime输出为本地时间戳
print(time.ctime(time.mktime(t)))

# 将时间按照自己定义的格式输出出来。
print(time.strftime("%Y-%m-%d %H:%M:%S", t))