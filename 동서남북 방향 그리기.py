# import turtle
#
# # 화면과 거북이 초기화
# screen = turtle.Screen()
# screen.title("Turtle 방향 예제")
# t = turtle.Turtle()
# t.pensize(2)
# t.speed(1)
#
# # 거리 설정
# length = 100
#
# # 동쪽 (기본 방향)
# t.color("red")
# t.write("동 (East)", font=("Arial", 12, "bold"))
# t.forward(length)
# t.backward(length)  # 중심으로 복귀
#
# # 북쪽
# t.left(90)  # 북쪽으로 회전
# t.color("blue")
# t.write("북 (North)", font=("Arial", 12, "bold"))
# t.forward(length)
# t.backward(length)
#
# # 서쪽
# t.left(90)  # 서쪽
# t.color("green")
# t.write("서 (West)", font=("Arial", 12, "bold"))
# t.forward(length)
# t.backward(length)
#
# # 남쪽
# t.left(90)  # 남쪽
# t.color("purple")
# t.write("남 (South)", font=("Arial", 12, "bold"))
# t.forward(length)
# t.backward(length)
#
# # 끝
# t.hideturtle()
# screen.exitonclick()  # 클릭 시 창 닫기


import turtle

# 화면 및 거북이 초기화
screen = turtle.Screen()
screen.title("Turtle 방향 예제")
t = turtle.Turtle()
t.pensize(2)
t.speed(1)

# 거리 설정
length = 100

# 동쪽 (East)
t.color("red")
t.penup()
t.goto(0, 0)           # 중심으로 이동
t.setheading(0)        # 동쪽
t.forward(length)      # 동쪽 끝으로 이동
t.pendown()
t.backward(length)     # 선 긋기 (중심까지)
t.penup()
t.forward(length + 10) # 텍스트 위치 약간 바깥쪽
t.write("동 (East)", align="center", font=("Arial", 12, "bold"))

# 북쪽 (North)
t.color("blue")
t.goto(0, 0)
t.setheading(90)
t.forward(length)
t.pendown()
t.backward(length)
t.penup()
t.forward(length + 10)
t.write("북 (North)", align="center", font=("Arial", 12, "bold"))

# 서쪽 (West)
t.color("green")
t.goto(0, 0)
t.setheading(180)
t.forward(length)
t.pendown()
t.backward(length)
t.penup()
t.forward(length + 10)
t.write("서 (West)", align="center", font=("Arial", 12, "bold"))

# 남쪽 (South)
t.color("purple")
t.goto(0, 0)
t.setheading(270)
t.forward(length)
t.pendown()
t.backward(length)
t.penup()
t.forward(length + 10)
t.write("남 (South)", align="center", font=("Arial", 12, "bold"))

# 마무리
t.hideturtle()
screen.exitonclick()
