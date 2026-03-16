"""
1、turtle(海龟)是Python重要的标准库之一，它能够进行基本的图形绘制。
2、turtle库绘制图形有一个基本框架:
一个小海龟在坐标系中爬行，其爬行轨迹形成了绘制图形。
对于小海龟来说，有“前进““后退”“旋转”等爬行行为，
对坐标系的探索也通过“前进方向““左侧方向”和“后退方向”、“右侧方向”等小海龟自身角度方位来完成。

一、turtle库的引用方式
第一种，import turtle，则对turtle库中函数调 用采用turtle.<函数名>()形式。
第二种，from turtle import *，则对turtle库中 函数调用直接采用<函数名>()形式，不在使用 turtle.作为前导。
第三种，import turtle as t，则对turtle库中函数 调用采用更简洁的t.<函数名>()形式，保留字as 的作用是将turtle库给予别名t。
"""
# 第一种(给一个库的接口，去调用)
import turtle
turtle.fd(200)

# 第二种(将目标库中的所有函数导入到本地（可以导入单独的目标函数），然后可以直接使用库中的函数)
from turtle import fd
from turtle import *
fd(200)

# 第三种(调用库接口，将库名称给与一个别名”t“)
import turtle as t
t.fd(200)

## 窗口函数
"""
turtle.setup(width(宽), height(高), startx(起始坐标),starty(终止坐标))  # 窗体函数
"""