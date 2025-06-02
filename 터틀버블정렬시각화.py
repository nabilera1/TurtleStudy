# 거품 정렬 시각화 (Bubble Sort Visualization)
# 문제 설명:
# turtle을 사용하여 거품 정렬(Bubble Sort)을 시각화하세요.
# 각 숫자를 직사각형 막대(bar)로 표현합니다.
# 두 막대를 비교하고 교환할 때 색상을 바꿔 시각적으로 강조합니다.
# 정렬이 완료되면 막대를 초록색으로 표시합니다.

import turtle
import random
import time

def draw_bars(t, data, color_array):
    t.clear()
    for i in range(len(data)):
        t.up()
        t.goto(-250 + i * 20, 0)
        t.down()
        t.fillcolor(color_array[i])
        t.begin_fill()
        t.goto(-250 + i * 20, data[i])
        t.goto(-250 + i * 20 + 15, data[i])
        t.goto(-250 + i * 20 + 15, 0)
        t.goto(-250 + i * 20, 0)
        t.end_fill()
    screen.update()
    time.sleep(0.1)

def bubble_sort_visual(t, data):
    n = len(data)
    for i in range(n):
        for j in range(n - i - 1):
            color_array = ['gray'] * len(data)
            color_array[j] = 'red'
            color_array[j+1] = 'red'
            draw_bars(t, data, color_array)
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    draw_bars(t, data, ['green'] * len(data))

# 터틀 세팅
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Bubble Sort Visualization")
screen.setup(width=600, height=400)
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

# 무작위 데이터 생성
data = [random.randint(10, 150) for _ in range(20)]

# 정렬 시각화 실행
bubble_sort_visual(t, data)

# 창을 닫지 않도록
screen.mainloop()


# 학습 포인트:
# turtle로 데이터를 막대그래프 형태로 시각화
#
# 정렬 알고리즘의 내부 과정을 애니메이션으로 이해
#
# 색상 활용을 통해 비교/교환 포인트 강조
#
# 정렬 완료 후 완성 상태 강조 표시