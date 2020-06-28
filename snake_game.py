# turtle used to draw lines
import turtle
#makes sure that the head doesnt move off the screen very quickly
import time

delay = 0.1
#setting up the screen

wn = turtle.Screen()
wn.title("Snake Game by Aryan")
wn.bgcolor("green")
wn.setup(height = 600, width = 600)
#turns off animation on the screen or the updates on the screen
wn.tracer(0)

#snake head

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
#makes sure that turtle does not draw any lines
head.penup()
#it will start at the centre
head.goto(0,0)
head.direction = "stop"


#functions(whenever function is called, head will move 20 pixels in the direction given)
def go_up():
	head.direction = "up"

def go_down():
	head.direction = "down"

def go_left():
	head.direction = "left"

def go_right():
	head.direction = "right"


def move():
	if head.direction == "up":
		y = head.ycor()
		head.sety(y + 20)

	if head.direction == "down":
		y = head.ycor()
		head.sety(y - 20)

	if head.direction == "left":
		x = head.xcor()
		head.setx(x - 20)

	if head.direction == "right":
		x = head.xcor()
		head.setx(x + 20)

#keyboard binds or buttons
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

#main game loop which will keep updating the screen
while True:
	wn.update()
move()


time.sleep(delay)







#this will keep the window open
wn.mainloop()
