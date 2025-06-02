# 재귀 삼각형 그리기 (Sierpinski Triangle)
# 문제 설명
# 터틀 그래픽을 사용하여 Sierpinski 삼각형을 재귀적으로 그리세요.
#
# 입력으로는 길이(length)와 깊이(depth)가 주어집니다.
#
# 깊이가 0이면 한 개의 정삼각형을 그립니다.
#
# 깊이가 1 이상이면 세 개의 삼각형으로 나누어 다시 재귀적으로 그립니다.

import turtle

def draw_triangle(points, color, t):
    t.fillcolor(color)
    t.up()
    t.goto(points[0][0], points[0][1])
    t.down()
    t.begin_fill()
    t.goto(points[1][0], points[1][1])
    t.goto(points[2][0], points[2][1])
    t.goto(points[0][0], points[0][1])
    t.end_fill()

def midpoint(p1, p2):
    return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]

def sierpinski(points, depth, t):
    colors = ['blue', 'red', 'green', 'yellow', 'purple', 'orange']
    draw_triangle(points, colors[depth % len(colors)], t)
    if depth > 0:
        sierpinski([points[0],
                    midpoint(points[0], points[1]),
                    midpoint(points[0], points[2])],
                   depth - 1, t)
        sierpinski([points[1],
                    midpoint(points[0], points[1]),
                    midpoint(points[1], points[2])],
                   depth - 1, t)
        sierpinski([points[2],
                    midpoint(points[2], points[1]),
                    midpoint(points[0], points[2])],
                   depth - 1, t)

# 터틀 설정
screen = turtle.Screen()
t = turtle.Turtle()
t.speed('fastest')

# 초기 삼각형 좌표
size = 300
initial_points = [[-size, -size/2], [0, size], [size, -size/2]]

# 삼각형 그리기
sierpinski(initial_points, depth=4, t=t)

screen.mainloop()

# 학습 포인트
# 재귀 분할의 개념을 시각적으로 이해 가능
# 좌표 계산과 재귀 호출의 조합
# Turtle을 이용한 좌표 기반 그래픽 그리기 연습
