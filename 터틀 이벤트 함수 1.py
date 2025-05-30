import turtle

# 거북이 생성
t = turtle.Turtle()
t.speed(2)  # 이동 속도 조절

# ⬆ 위쪽 이동
def move_up():
    t.setheading(90)    # 위쪽 (북)
    t.forward(50)

# ⬇ 아래쪽 이동
def move_down():
    t.setheading(270)   # 아래쪽 (남)
    t.forward(50)

# ⬅ 왼쪽 이동
def move_left():
    t.setheading(180)   # 왼쪽 (서)
    t.forward(50)

# ➡ 오른쪽 이동
def move_right():
    t.setheading(0)     # 오른쪽 (동)
    t.forward(50)

# 🧹 화면 초기화 (선 지우기, 거북이 위치 유지)
def clear_screen():
    t.clear()

# 🔄 거북이 초기화 (위치, 방향, 그린 것 모두)
def reset_turtle():
    t.reset()

# ❌ 프로그램 종료
def quit_program():
    turtle.bye()

# 이벤트 바인딩
screen = turtle.Screen()
screen.listen()  # 키 입력 감지 시작

# 방향키
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# 기타 기능 키
screen.onkey(clear_screen, "c")   # c 키: 화면 지우기
screen.onkey(reset_turtle, "r")   # r 키: 거북이 리셋
screen.onkey(quit_program, "q")   # q 키: 종료

# 창 유지
screen.mainloop()
