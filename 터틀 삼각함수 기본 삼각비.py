# import turtle
# import math
#
# turtle.speed(0)
# turtle.hideturtle()
#
# # 단위원 반지름
# r = 100
#
# # 단위원 그리기
# turtle.penup()
# turtle.goto(0, -r)
# turtle.pendown()
# turtle.circle(r)
#
# # 각도 설정
# theta_deg = 60
# theta_rad = math.radians(theta_deg)
#
# # 단위원 위 점 좌표
# x = r * math.cos(theta_rad)
# y = r * math.sin(theta_rad)
#
# # 중심에서 점까지 선
# turtle.penup()
# turtle.goto(0, 0)
# turtle.pendown()
# turtle.goto(x, y)
# turtle.dot(8, "red")
#
# # cos 선 (x축 그림자)
# turtle.penup()
# turtle.goto(0, 0)
# turtle.setheading(0)
# turtle.forward(x)
# turtle.dot(5, "blue")  # cos 값 점
#
# # sin 선 (y축 높이)
# turtle.penup()
# turtle.goto(x, 0)
# turtle.pendown()
# turtle.goto(x, y)
# turtle.dot(5, "green")  # sin 값 점
#
# turtle.done()


import turtle
import math

turtle.speed(0)
turtle.hideturtle()

# 좌표 축 그리기
turtle.penup()
turtle.goto(-360, 0)
turtle.pendown()
turtle.goto(360, 0)
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.goto(0, 100)

# sin 그래프 그리기
turtle.penup()
for x in range(-360, 361):
    y = 100 * math.sin(math.radians(x)) # vs math.sin(theta_rad)
    turtle.goto(x, y)
    turtle.pendown()

turtle.done()
