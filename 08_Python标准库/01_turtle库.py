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
# fd(200): 表示向前走(200个像素)
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
作用:设置主窗体的大小和位置 参数:
    width : 窗口宽度，如果值是整数，表示的像素值;如果值 是小数，表示窗口宽度与屏幕的比例;
    height: 窗口高度，如果值是整数，表示的像素值;如果 值是小数，表示窗口高度与屏幕的比例;
    startx: 窗口左侧与屏幕左侧的像素距离，如果值是None，窗口位于屏幕水平中央;
    starty: 窗口顶部与屏幕顶部的像素距离，如果值是None，窗口位于屏幕垂直中央;
"""
# 窗口函数使用
import turtle
# turtle.setup(200, 100, 100, 100)
# setup()表示打开窗口
turtle.setup(0.8, 0.8, 100, 100)

# turtle.done() 和 turtle.mainloop() 作用相同，都会启动 turtle 的事件循环，使窗口保持响应。
# 如果你在交互式环境（如 IDLE、Jupyter Notebook）中逐行执行，窗口可能不会立即关闭，因为 Python 进程仍在运行。
# 但在脚本模式下（直接运行 .py 文件）必须调用上述done函数。
turtle.done()

