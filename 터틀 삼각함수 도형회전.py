

import turtle
import math

# 설정
turtle.speed(0)
turtle.hideturtle()

# 회전 함수: 점 (x, y)를 각도 angle만큼 회전시킨 결과 반환
# 중심(0, 0)을 기준으로 점을 회전시킵니다.
def rotate(x, y, angle_deg):
    angle_rad = math.radians(angle_deg)
    x_new = x * math.cos(angle_rad) - y * math.sin(angle_rad)
    y_new = x * math.sin(angle_rad) + y * math.cos(angle_rad)
    # 회전공식
    return x_new, y_new

# 삼각형 꼭짓점 정의 (원점 기준)
triangle = [(100, 0), (50, 100), (-50, 50)]

# 삼각형을 여러 각도로 회전시키며 그림
for angle in range(0, 360, 30):
    rotated = [rotate(x, y, angle) for (x, y) in triangle]
    turtle.penup()
    turtle.goto(rotated[-1])
    turtle.pendown()
    for x, y in rotated:
        turtle.goto(x, y)
    turtle.goto(rotated[0])  # 삼각형 닫기

turtle.done()



