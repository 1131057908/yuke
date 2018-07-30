



# my_set_2={1,2,3,4,5,6,2,7,9,8}
#
#
# res=my_set_2.discard(2)
# print(res)
#小海龟
#运动命令 forward；向前运动  backward；向后运动
#right向右， left 向左转多少度
#goto 移动到坐标为（x，y）的位置
#speed  向左笔画移动速度
#up 笔画抬起
#down 笔画落下
#pensize()
#pencolor()
#setheading()改变海归的朝向
#绘图窗口的零点在正中间，默认海归方向向右
import turtle
turtle.forward(100)
turtle.right(45)
turtle.forward(100)
turtle.goto(-100,-200)

turtle.speed(100)
turtle.up()
turtle.goto(-100,100)


turtle.down()
turtle.circle(100,steps=5)
turtle.begin_fill()
turtle.fillcolor("blue")
turtle.end_fill()
turtle.pensize(10)
turtle.pencolor("blue")
turtle.forward(105)
turtle.circle(100,steps=3)
turtle.forward(200)

turtle.setheading(20)
#turtle,circle(r,e)r 为半径  e为次数可不填写几边形

turtle.undo()#撤销上




# turtle.reset()  #恢复默认值，重置title()
turtle.done()#保证程序不断运行

# turtle.clear()  #回复默认值，不重置title