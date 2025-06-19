import turtle

# 화면 설정
screen = turtle.Screen()
screen.setworldcoordinates(-20, -10, 10, 100)  # 좌표계 설정 (x축, y축 범위)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# 좌표축 그리기
t.penup()
t.goto(-20, 0)
t.pendown()
t.goto(10, 0)  # x축
t.penup()
t.goto(0, -10)
t.pendown()
t.goto(0, 100)  # y축

# 함수 정의
def f(x):
    return x**2 + 10*x + 25

# 함수 그래프 그리기
t.penup()
for x in range(-20, 11):  # x값 -20부터 10까지
    y = f(x)
    t.goto(x, y)
    t.pendown()

turtle.done()
