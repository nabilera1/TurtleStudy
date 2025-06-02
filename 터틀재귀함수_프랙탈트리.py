import turtle

def draw_tree(branch_length, t):
    if branch_length > 5:
        # 줄기 그리기
        t.forward(branch_length)
        # 오른쪽 가지
        t.right(20)
        draw_tree(branch_length - 15, t)
        # 왼쪽 가지
        t.left(40)
        draw_tree(branch_length - 15, t)
        # 원래 방향으로 되돌아오기
        t.right(20)
        t.backward(branch_length)

# 터틀 세팅
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.color("green")
t.speed("fastest")
t.left(90)  # 위쪽으로 향하도록
t.up()
t.backward(100)
t.down()

# 트리 그리기
draw_tree(75, t)

# 창을 닫지 않도록
screen.mainloop()



# draw_tree 함수는 재귀적으로 가지를 그리고,
# 각 단계마다 길이를 줄이며 각도를 조절합니다.
# branch_length가 작아지면 재귀 호출을 멈추도록 종료 조건을 설정합니다.
# turtle의 방향과 위치를 조정해 가지를 그린 뒤 원래 위치로 되돌아옵니다.