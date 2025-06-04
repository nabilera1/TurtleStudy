import turtle

# 삼각형 (바람개비 날개 하나)
# points = [(0, 0), (0, 120), (30, 30)]
points = [(0, 0), (60, 0), (120, 60)]
pinwheel_shape = turtle.Shape("polygon", points)
turtle.register_shape("pinwheel", pinwheel_shape)

# 거북이 설정
t = turtle.Turtle()
t.shape("pinwheel")
t.color("red", "yellow")
t.penup()
t.speed(0)
t.goto(0, 0)

angle = 0
stamp_ids = []

def rotate():
    global angle, stamp_ids

    # 이전 도장 제거
    for sid in stamp_ids:
        t.clearstamp(sid)
    stamp_ids = []

    # 4개의 날개를 찍음 (각도 차이 90도)
    for offset in range(0, 360, 90):
        t.setheading(angle + offset)
        stamp_id = t.stamp()
        stamp_ids.append(stamp_id)

    angle = (angle + 10) % 360  # 회전 속도 조절
    turtle.ontimer(rotate, 50)  # 20 fps

rotate()

t.hideturtle()
turtle.done()


# 중앙에서 날개 4개가 90도 간격으로 회전하면서 도장 찍힘
#
# 도장을 반복적으로 갱신하며 전체 바람개비처럼 회전
#
# 진짜 날개 4개가 도는 애니메이션처럼 보입니다 🌀