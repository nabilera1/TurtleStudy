# 단위원 위의 각 𝜃=45 에서의 점 P를 turtle을 이용하여 그리시오. (단위원 반지름 = 100)

import turtle
import math

turtle.speed(0)
turtle.hideturtle()

# 단위원 그리기
radius = 100
turtle.penup()
turtle.goto(0, -radius)
turtle.pendown()
turtle.circle(radius)

# 각도 θ
theta_deg = 45
theta_rad = math.radians(theta_deg)
print(theta_rad)
# 점 P 계산
x = radius * math.cos(theta_rad)
y = radius * math.sin(theta_rad)

# 점 P 표시
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.goto(x, y)
turtle.dot(10, "red")
turtle.done()
