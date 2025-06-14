#숫자를 입력하면 패턴을 그리는 프로그램
import turtle
import time
import random

print ("숫자를 입력하면 패턴을 그려요")
num_str = input("숫자 입력 : ")
if num_str.isdigit():
	squares = int(num_str)

angle = 180 - 180*(squares-2)/squares

turtle.up()

x = 0
y = 0
turtle.setpos(x, y)


numshapes = 8
for x in range(numshapes):
	turtle.color(random.random(), random.random(), random.random())
	x += 5
	y += 5
	turtle.forward(x)
	turtle.left(y)
	for i in range(squares):
		turtle.begin_fill()
		turtle.down()
		turtle.forward(40)
		turtle.left(angle)
		turtle.forward(40)
		print (turtle.pos())
		turtle.up()
		turtle.end_fill()

time.sleep(3)
# turtle.bye()
turtle.done()