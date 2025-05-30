import turtle

turtle.setup(480, 320) # 캔버스 크기 설정
my_window = turtle.Screen() # 윈도우 이름 설정
my_window.title("절대 위치로 그리기")

t = turtle.Turtle() # 터틀 생성
# t.penup()
t.setposition(100, 0)
t.setposition(50, 86.6)
t.setposition(0, 0)
turtle.mainloop()