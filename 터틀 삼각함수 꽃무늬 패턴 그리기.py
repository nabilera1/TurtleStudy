# 이 코드는 극좌표 방정식 r=cos(3θ)를 이용하여 "로터스 꽃" 같은 패턴을 만듭니다.

import turtle
import math

turtle.speed(0)
turtle.bgcolor("white")
turtle.pensize(2)

# 꽃잎 그리기
for angle in range(0, 360, 10):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pencolor("black")
    theta = math.radians(angle)
    x = 150 * math.cos(3 * theta) * math.cos(theta)
    y = 150 * math.cos(3 * theta) * math.sin(theta)
    turtle.pendown()
    turtle.goto(x, y)

turtle.hideturtle()
turtle.done()
