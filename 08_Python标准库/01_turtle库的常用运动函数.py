"""
函数                                  描述
forward()                            沿着当前指定方向前进距离
backward()                           沿着当前相反方向后退指定距离
setheading(angle)                    设置当前朝向为angle角度
circle(r,e)                          绘制一个半径r和角度e得圆或弧形
undo()                               撤销画笔最后一步动作
right(angle)                         向右旋转angle角度
left(angle)                          向左旋转angle角度
goto(x,y)                            移动到绝对坐标(x,y)处
speed()                              设置画笔得绘制速度，参数为0-10
dot(d,color)                         绘制一个直径d和颜色color的圆点
home()                               设置当前画笔位置为原点，朝向东
"""
## forward();backward();setheading(angle)
from turtle import *

forward(100)
backward(200)
setheading(90)
forward(100)

# setheading()写多个也是朝着固定的方向。
# right()和left(),每次都会在上一次的基础上进行旋转。

## right(angle);left(angle)
from turtle import *

left(90)
forward(100)
left(90)
forward(200)

## cricle()
from turtle import *

circle(100, 360)
# 撤销上一步的操作
undo()

## goto()
from turtle import *

# 移动到指定位置，画笔方向不变
goto(100, 100)

## speed();
from turtle import *
speed(10)  # 0 10 6 3 1 ,快---慢
circle(100, 360)

## dot(d,color)
from turtle import *
dot(10, "blue")

## home()；home回到原点也会画出一条线
from turtle import *
left(60)
forward(200)
left(60)
forward(200)
home()





