import turtle #Inside_Out
w = turtle.Screen()
w.bgcolor("light green")
t = turtle.Turtle()
t.color("blue")

def 나선사각형(size):
	for i in range(4):
		t.fd(size)
		t.left(90)
		size = size + 5

나선사각형(6)
나선사각형(26)
나선사각형(46)
나선사각형(66)
나선사각형(86)
나선사각형(106)
나선사각형(126)
나선사각형(146)

turtle.done()