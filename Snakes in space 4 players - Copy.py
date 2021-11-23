# importing modules
import turtle
import time
import random

# food in the game
food = turtle.Turtle()
colors = random.choice(['white'])
shapes = random.choice(['circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 0)

# text in the game
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("player1 : 0 player2 : 0 player3 : 0 player4 : 0", align="center", font=("candara", 24, "bold"))

# setup
running = True
while running:
	wn = turtle.Screen()
	wn.title("SnakesInSpace")
	wn.bgcolor("black")
	wn.setup(width=1200, height=600)
	wn.tracer(0)
	delay1 = 0.1
	score = 0
	player2 = 0
	player3 = 0
	player4 = 0

	# snake1 code
	snake1 = turtle.Turtle()
	snake1.shape("square")
	snake1.color("red")
	snake1.penup()
	snake1.goto(315, 270)
	snake1.direction = "Stop"

	# snake2 code
	snake2 = turtle.Turtle()
	snake2.shape("square")
	snake2.color("yellow")
	snake2.penup()
	snake2.goto(-315, -270)
	snake2.direction = "Stop"

	# snake3 code
	snake3 = turtle.Turtle()
	snake3.shape("square")
	snake3.color("blue")
	snake3.penup()
	snake3.goto(315, -270)
	snake3.direction = "Stop"

	# snake4 code
	snake4 = turtle.Turtle()
	snake4.shape("square")
	snake4.color("pink")
	snake4.penup()
	snake4.goto(-315, 270)
	snake4.direction = "Stop"

	# assigning key directions for snake1
	
	# snake1 going up
	def goup1():
		if snake1.direction != "down":
			snake1.direction = "up"
	
	# snake1 going down
	def godown1():
		if snake1.direction != "up":
			snake1.direction = "down"
	
	# snake1 going left
	def goleft1():
		if snake1.direction != "right":
			snake1.direction = "left"
	
	# snake1 going right
	def goright1():
		if snake1.direction != "left":
			snake1.direction = "right"
	
	# snake1 moving in general
	def move1():
		if snake1.direction == "up":
			y1 = snake1.ycor()
			snake1.sety(y1 + 20)
		if snake1.direction == "down":
			y1 = snake1.ycor()
			snake1.sety(y1 - 20)
		if snake1.direction == "left":
			x1 = snake1.xcor()
			snake1.setx(x1 - 20)
		if snake1.direction == "right":
			x1 = snake1.xcor()
			snake1.setx(x1 + 20)


	# assigning key directions for snake2

	def goup2():
		if snake2.direction != "down":
			snake2.direction = "up"


	def godown2():
		if snake2.direction != "up":
			snake2.direction = "down"


	def goleft2():
		if snake2.direction != "right":
			snake2.direction = "left"


	def goright2():
		if snake2.direction != "left":
			snake2.direction = "right"


	def move2():
		if snake2.direction == "up":
			y2 = snake2.ycor()
			snake2.sety(y2 + 20)
		if snake2.direction == "down":
			y2 = snake2.ycor()
			snake2.sety(y2 - 20)
		if snake2.direction == "left":
			x2 = snake2.xcor()
			snake2.setx(x2 - 20)
		if snake2.direction == "right":
			x2 = snake2.xcor()
			snake2.setx(x2 + 20)
	
	# assigning key directions for snake3
	
	def goup3():
		if snake3.direction != "down":
			snake3.direction = "up"


	def godown3():
		if snake3.direction != "up":
			snake3.direction = "down"


	def goleft3():
		if snake3.direction != "right":
			snake3.direction = "left"


	def goright3():
		if snake3.direction != "left":
			snake3.direction = "right"


	def move3():
		if snake3.direction == "up":
			y3 = snake3.ycor()
			snake3.sety(y3 + 20)
		if snake3.direction == "down":
			y3 = snake3.ycor()
			snake3.sety(y3 - 20)
		if snake3.direction == "left":
			x3 = snake3.xcor()
			snake3.setx(x3 - 20)
		if snake3.direction == "right":
			x3 = snake3.xcor()
			snake3.setx(x3 + 20)


	# assigning key directions for snake4

	def goup4():
		if snake4.direction != "down":
			snake4.direction = "up"


	def godown4():
		if snake4.direction != "up":
			snake4.direction = "down"


	def goleft4():
		if snake4.direction != "right":
			snake4.direction = "left"


	def goright4():
		if snake4.direction != "left":
			snake4.direction = "right"


	def move4():
		if snake4.direction == "up":
			y4 = snake4.ycor()
			snake4.sety(y4 + 20)
		if snake4.direction == "down":
			y4 = snake4.ycor()
			snake4.sety(y4 - 20)
		if snake4.direction == "left":
			x4 = snake4.xcor()
			snake4.setx(x4 - 20)
		if snake4.direction == "right":
			x4 = snake4.xcor()
			snake4.setx(x4 + 20)


	# waiting for controls
	wn.listen()
	wn.onkeypress(goup1, "i")
	wn.onkeypress(godown1, "k")
	wn.onkeypress(goleft1, "j")
	wn.onkeypress(goright1, "l")
	wn.onkeypress(goup2, "w")
	wn.onkeypress(godown2, "s")
	wn.onkeypress(goleft2, "a")
	wn.onkeypress(goright2, "d")
	wn.onkeypress(goup3, "Up")
	wn.onkeypress(godown3, "Down")
	wn.onkeypress(goleft3, "Left")
	wn.onkeypress(goright3, "Right")
	wn.onkeypress(goup4, "t")
	wn.onkeypress(godown4, "g")
	wn.onkeypress(goleft4, "f")
	wn.onkeypress(goright4, "h")
	segment1 = []
	segment2 = []
	segment3 = []
	segment4 = []
	
	# mainloop
	while running:
		wn.update()
		if snake1.xcor() > 580 or snake1.xcor() < -580 or snake1.ycor() > 290 or snake1.ycor() < -290:
			time.sleep(1)
			snake1.goto(0, 0)
			score -= 10
			snake1.direction = "Stop"
			for segment in segment1:
				segment.goto(1000, 1000)
			segment1.clear()
			delay1 = 0.1
			pen.clear()
			pen.write("player1 : {} player2 : {} player3 : {} player4 : {} ".format(score, player2, player3, player4),
					  align="center", font=("candara", 22, "bold"))
		if snake2.xcor() > 580 or snake2.xcor() < -580 or snake2.ycor() > 290 or snake2.ycor() < -290:
			time.sleep(1)
			snake2.goto(0, 0)
			player2 -= 10
			snake2.direction = "Stop"
			for segment in segment2:
				segment.goto(1000, 1000)
			segment2.clear()
			delay1 = 0.1
			pen.clear()
			pen.write("player1 : {} player2 : {} player3 : {} player4 : {} ".format(score, player2, player3, player4),
					  align="center", font=("candara", 22, "bold"))
		if snake3.xcor() > 580 or snake3.xcor() < -580 or snake3.ycor() > 290 or snake3.ycor() < -290:
			time.sleep(1)
			snake3.goto(0, 0)
			player3 -= 10
			snake3.direction = "Stop"
			delay1 = 0.1
			pen.clear()
			pen.write("player1 : {} player2 : {} player3 : {} player4 : {} ".format(score, player2, player3, player4),
					  align="center", font=("candara", 22, "bold"))
			for segment in segment3:
				segment.goto(1000, 1000)
			segment3.clear()
		if snake4.xcor() > 580 or snake4.xcor() < -580 or snake4.ycor() > 290 or snake4.ycor() < -290:
			time.sleep(1)
			snake4.goto(0, 0)
			player4 -= 10
			snake4.direction = "Stop"
			delay1 = 0.1
			pen.clear()
			pen.write("player1 : {} player2 : {} player3 : {} player4 : {} ".format(score, player2, player3, player4),
					  align="center", font=("candara", 22, "bold"))
			for segment in segment4:
				segment.goto(1000, 1000)
			segment4.clear()
		if snake1.distance(food) < 20:
			x1 = random.randint(-540, 540)
			y1 = random.randint(-270, 270)
			food.goto(x1, y1)
			new_segment1 = turtle.Turtle()
			new_segment1.speed(0)
			new_segment1.shape("square")
			new_segment1.color("orange")
			new_segment1.penup()
			segment1.append(new_segment1)
			delay1 -= 0.001
			score += 10
			pen.clear()
			pen.write("player1 : {} player2 : {} player3 : {} player4 : {} ".format(score, player2, player3, player4),
					  align="center", font=("candara", 22, "bold"))
		if snake2.distance(food) < 20:
			x2 = random.randint(-540, 540)
			y2 = random.randint(-270, 270)
			food.goto(x2, y2)
			new_segment2 = turtle.Turtle()
			new_segment2.speed(0)
			new_segment2.shape("square")
			new_segment2.color("green")
			new_segment2.penup()
			segment2.append(new_segment2)
			delay1 -= 0.001
			player2 += 10
			pen.clear()
			pen.write("player1 : {} player2 : {} player3 : {} player4 : {} ".format(score, player2, player3, player4),
					  align="center", font=("candara", 22, "bold"))
		if snake3.distance(food) < 20:
			x3 = random.randint(-520, 520)
			y3 = random.randint(-270, 270)
			food.goto(x3, y3)
			new_segment3 = turtle.Turtle()
			new_segment3.speed(0)
			new_segment3.shape("square")
			new_segment3.color("purple")
			new_segment3.penup()
			segment3.append(new_segment3)
			delay1 -= 0.001
			player3 += 10
			pen.clear()
			pen.write("player1 : {} player2 : {} player3 : {} player4 : {} ".format(score, player2, player3, player4),
					  align="center", font=("candara", 22, "bold"))
		if snake4.distance(food) < 20:
			x4 = random.randint(-520, 520)
			y4 = random.randint(-270, 270)
			food.goto(x4, y4)
			new_segment4 = turtle.Turtle()
			new_segment4.speed(0)
			new_segment4.shape("square")
			new_segment4.color("brown")
			new_segment4.penup()
			segment4.append(new_segment4)
			delay1 -= 0.001
			player4 += 10
			pen.clear()
			pen.write("player1 : {} player2 : {} player3 : {} player4 : {} ".format(score, player2, player3, player4),
					  align="center", font=("candara", 22, "bold"))
		# Checking for snake1 collisions with body segment1
		for index in range(len(segment1) - 1, 0, -1):
			x1 = segment1[index - 1].xcor()
			y1 = segment1[index - 1].ycor()
			segment1[index].goto(x1, y1)
		for index in range(len(segment2) - 1, 0, -1):
			x2 = segment2[index - 1].xcor()
			y2 = segment2[index - 1].ycor()
			segment2[index].goto(x2, y2)
		for index in range(len(segment3) - 1, 0, -1):
			x3 = segment3[index - 1].xcor()
			y3 = segment3[index - 1].ycor()
			segment3[index].goto(x3, y3)
		for index in range(len(segment4) - 1, 0, -1):
			x4 = segment4[index - 1].xcor()
			y4 = segment4[index - 1].ycor()
			segment4[index].goto(x4, y4)
		if len(segment1) > 0:
			x1 = snake1.xcor()
			y1 = snake1.ycor()
			segment1[0].goto(x1, y1)
		move1()
		if len(segment2) > 0:
			x2 = snake2.xcor()
			y2 = snake2.ycor()
			segment2[0].goto(x2, y2)
		move2()
		if len(segment3) > 0:
			x3 = snake3.xcor()
			y3 = snake3.ycor()
			segment3[0].goto(x3, y3)
		move3()
		if len(segment4) > 0:
			x4 = snake4.xcor()
			y4 = snake4.ycor()
			segment4[0].goto(x4, y4)
		move4()
		for segment in segment1:
			if segment.distance(snake1) < 20:
				time.sleep(1)
				snake1.goto(0, 0)
				snake1.direction = "stop"
				score -= 10
				wn.update()
				for segment in segment1:
					segment.goto(1000, 1000)
				segment1.clear()
		for segment in segment2:
			if segment.distance(snake2) < 20:
				time.sleep(1)
				snake2.goto(0, 0)
				snake2.direction = "stop"
				player2 -= 10
				wn.update()
				for segment in segment2:
					segment.goto(1000, 1000)
				segment2.clear()
		for segment in segment3:
			if segment.distance(snake3) < 20:
				time.sleep(1)
				snake3.goto(0, 0)
				snake3.direction = "stop"
				player3 -= 10
				wn.update()
				for segment in segment3:
					segment.goto(1000, 1000)
				segment3.clear()
		for segment in segment4:
			if segment.distance(snake4) < 20:
				time.sleep(1)
				snake4.goto(0, 0)
				snake4.direction = "stop"
				player4 -= 10
				wn.update()
				for segment in segment4:
					segment.goto(1000, 1000)
				segment4.clear()
				delay1 = 0.1
				pen.clear()
				pen.write(
					"player1 : {} player2 : {} player3 : {} player4 : {} ".format(score, player2, player3, player4),
					align="center", font=("candara", 22, "bold"))
		if score >= 500:
			pen.setpos(-50, 100)
			pen.color("green")
			pen.write("Player 1 wins", font=("candara", 22, "bold"))
			delay1 += 4
			running = False
		if player2 >= 500:
			pen.setpos(-50, 100)
			pen.color("green")
			pen.write("Player 2 wins", font=("candara", 22, "bold"))
			delay1 += 4
			running = False
		if player3 >= 500:
			pen.setpos(-50, 100)
			pen.color("green")
			pen.write("Player 3 wins", font=("candara", 22, "bold"))
			delay1 += 4
			running = False
		if player4 >= 500:
			pen.setpos(-50, 100)
			pen.color("green")
			pen.write("Player 4 wins", font=("candara", 22, "bold"))
			delay1 += 4
			running = False
		time.sleep(delay1)
