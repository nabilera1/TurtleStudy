# import turtle
# import math
#
# # 설정
# turtle.speed(1)
# turtle.hideturtle()
#
# # 회전 함수
# def rotate_point(x, y, angle_deg):
#     angle_rad = math.radians(angle_deg)
#     new_x = x * math.cos(angle_rad) - y * math.sin(angle_rad)
#     new_y = x * math.sin(angle_rad) + y * math.cos(angle_rad)
#     return new_x, new_y
#
# # 원래 선 그리기
# x, y = 100, 0  # 시작점: 오른쪽으로 100만큼
# turtle.penup()
# turtle.goto(0, 0)
# turtle.pendown()
# turtle.goto(x, y)
#
# # 회전 후 선 그리기 (30도 회전)
# x2, y2 = rotate_point(x, y, 30)
# turtle.penup()
# turtle.goto(0, 0)
# turtle.pencolor("red")
# turtle.pendown()
# turtle.goto(x2, y2)
#
# turtle.done()



import math

angle = 30
radian = math.radians(angle)  # 도(degree)를 라디안으로 변환

x = 100
y = 0

# 회전 공식을 적용
new_x = x * math.cos(radian) - y * math.sin(radian)
new_y = x * math.sin(radian) + y * math.cos(radian)

print(new_x, new_y)  # 약 (86.6, 50.0) 회전된 좌표 
# 원래 x축 위에 있던 점이, 30도만큼 반시계방향으로 돌아가면 (86.6, 50.0) 위치로 이동합니다.

