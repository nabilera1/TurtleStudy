
import turtle

# 창 설정
screen = turtle.Screen()
screen.title("Turtle Example")
screen.bgcolor("lightblue")

# 거북이 생성
t = turtle.Turtle()
t.color("darkgreen")
t.pensize(3)

# 삼각형 그리기
for _ in range(3):
    t.forward(100)  # 앞으로 100픽셀 이동
    t.left(120)     # 왼쪽으로 120도 회전

# 창을 클릭할 때까지 유지
screen.exitonclick()



# import turtle: turtle 모듈을 가져옵니다.
#
# turtle.Screen(): 그래픽 창을 생성합니다.
#
# turtle.Turtle(): 거북이 객체를 생성합니다.
#
# t.forward(distance): 주어진 거리만큼 앞으로 이동.
#
# t.left(angle): 왼쪽으로 특정 각도만큼 회전.
#
# screen.exitonclick(): 사용자가 창을 클릭할 때까지 프로그램 종료를 대기합니다.
