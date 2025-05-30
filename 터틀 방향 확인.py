# import turtle
#
# t = turtle.Turtle()
# print(t.heading())  # 출력: 0.0
#
# t.left(90)
# print(t.heading())  # 출력: 90.0 (북쪽)
#
# t.right(180)
# print(t.heading())  # 출력: 270.0 (남쪽)
#
# turtle.done()

import turtle
import time

# 거북이 초기화
t = turtle.Turtle()
t.pensize(3)
t.speed(1)

# 텍스트 출력 함수
def write_heading(label):
    t.write(label, align="center", font=("Malgun Gothic", 14, "bold"))

# 1. 초기 방향: 동쪽 (0도)
t.setheading(0)
write_heading("동 (East) — 0도")
time.sleep(1)
t.clear()

# 2. 왼쪽으로 90도 (북쪽)
t.left(90)
write_heading("북 (North) — 90도")
time.sleep(1)
t.clear()

# 3. 오른쪽으로 180도 (남쪽)
t.right(180)
write_heading("남 (South) — 270도")
time.sleep(1)
t.clear()

# 4. 추가로 서쪽 방향도 확인
t.right(90)  # 현재 270도 → 180도 (서쪽)
write_heading("서 (West) — 180도")
time.sleep(1)
t.clear()

# 마무리
t.hideturtle()
turtle.done()
