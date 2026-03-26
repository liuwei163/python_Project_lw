import time
t = time.localtime()
print(time.mktime(t))
print(time.ctime(time.mktime(t)))
print(time.strftime("%Y-%m-%d %H:%M:%S", t))
