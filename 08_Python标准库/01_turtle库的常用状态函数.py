"""
函数                          描述
pendown()                    放下画笔
penup()                      拿起画笔
pensize()                    设置画笔线条的粗细
pencolor()                   设置画笔颜色
color()                      设置画笔和填充颜色
begin_fi()                   填充图形前，调用该方法
end fill()                   填充图形结束
filing()                     返回填充状态，True为填充
clear()                      清空当前窗口
"""

## pendown()和 penup()
import turtle
# 拿起画笔
turtle.up()
turtle.fd(200)
turtle.down()
turtle.fd(200)

turtle.done()

## pensize()
import turtle

turtle.pensize(5)
turtle.fd(200)

turtle.done()

## pencolor()
import turtle

turtle.pencolor("red")
turtle.fd(200)

turtle.done()

## color(); begin_fi(); end fill(); turtle.filling(); clear()
import turtle

# color("")：1.设置画笔颜色，2.设置填充颜色
turtle.color("blue", "red")
# 填充开始
turtle.begin_fill()

# 绘制一个三角形
for i in range(3):
    turtle.fd(100)
    turtle.left(120)

# 返回填充是否正常，成功填充返回True，失败则返回False
turtle.filling()

# 填充结束
turtle.end_fill()

# 清空窗口
turtle.clear()

turtle.done()

"""
reset()                         清空当前窗口，并重置位置
write(str,font=None)            输出font字体的字符串
screensize()                    设置画布的长和宽
hideturtle()                    隐藏画笔的turtle形状
showturtle                      显示画笔形状
isvisible()                     如果画笔可见则显示true
"""

## reset()
import turtle

# color("")：1.设置画笔颜色，2.设置填充颜色
turtle.color("blue")
turtle.fd(300)
# 清空窗口,并重置画笔位置
turtle.reset()

turtle.done()

## write(str,font=None)：输出font字体的字符串，screensize()：设置画布的长和宽
import turtle

turtle.write("liuwei")
turtle.screensize(1000, 1000)

turtle.done()

## hideturtle()：隐藏画笔；showturtle()：显示画笔
## isvisible()
import turtle

turtle.hideturtle()  # 隐藏画笔
turtle.fd(100)
# turtle.showturtle()  # 显示画笔

print(turtle.isvisible())  # 画笔可见即打印True；不可见即打印False

turtle.done()
