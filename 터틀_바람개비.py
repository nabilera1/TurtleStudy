# import turtle
#
# # 화면 초기화
# screen = turtle.Screen()
# screen.bgcolor("white")
#
# # 바람개비 모양 좌표 정의 (삼각형 날개)
# points = [(0, 0), (60, 0), (120, 60), (60, 60)]
#
# # 사용자 정의 도형 등록
# turtle.register_shape("pinwheel", points)
#
# # 거북이 설정
# t = turtle.Turtle()
# t.shape("pinwheel")           # 바람개비 모양 지정
# t.color("red", "yellow")      # 선색: 빨강, 채우기: 노랑
# t.penup()
# t.speed(0)                    # 최대 속도
#
# # 화면 중심에서 여러 방향으로 회전하며 찍기
# for angle in range(0, 360, 30):  # 0도부터 330도까지 30도 간격
#     t.setheading(angle)          # 방향 설정
#     t.stamp()                    # 도형 복사 (도장 찍기)
#
# # 종료 대기
# t.hideturtle()
# turtle.done()

# import turtle
#
# # 바람개비 날개 좌표 (삼각형 모양 → 시작점으로 돌아옴)
# points = [(0, 0), (60, 0), (0, 120)]
#
# # 사용자 도형 등록
# turtle.register_shape("pinwheel", points)
#
# # 거북이 생성 및 설정
# t = turtle.Turtle()
# t.shape("pinwheel")
# t.color("red", "yellow")
# t.penup()
# t.speed(0)
#
# # 회전하며 도장 찍기
# for angle in range(0, 360, 30):  # 12개 찍기
#     t.setheading(angle)
#     t.stamp()
#
# # 종료
# t.hideturtle()
# turtle.done()
import turtle

# 바람개비 삼각형 날개 좌표 (시작점으로 돌아오는 폐곡선)
points = [(0, 0), (60, 0), (120, 60)] #

# Shape 객체로 명시적으로 등록
s = turtle.Shape("polygon", points)
turtle.register_shape("pinwheel", s)  # 정상 등록!

# 거북이 생성 및 설정
t = turtle.Turtle()
t.shape("pinwheel")            # 사용자 정의 도형 사용
t.color("red", "yellow")       # 외곽선: 빨강, 채움: 노랑
t.penup()
t.speed(0)

# 회전하며 화면에 도장 찍기
for angle in range(0, 360, 30):
    t.setheading(angle)
    t.stamp()

# 종료
t.hideturtle()
turtle.done()
