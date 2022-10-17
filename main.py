import turtle

# making window
window = turtle.Screen()
window.title("pingo pongo")
window.bgcolor("black")
window.setup(800, 600)
window.tracer(0)

# making racque1
racquet1 = turtle.Turtle()
racquet1.speed(0)
racquet1.shape("square")
racquet1.color("blue")
racquet1.shapesize(5, 1)
racquet1.penup()
racquet1.goto(-350, 0)
# making racque2
racquet2 = turtle.Turtle()
racquet2.speed(0)
racquet2.shape("square")
racquet2.color("red")
racquet2.shapesize(5, 1)
racquet2.penup()
racquet2.goto(350, 0)
# making ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.goto(0, 0)
ball.penup()
ball.dx = .3
ball.dy = .3

# score
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score1 = 0
score2 = 0

score.write("{} : {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))


# movements of racquet1
def move_racquet1_up():
    y = racquet1.ycor()
    racquet1.sety(y + 20)


def move_racquet1_down():
    y = racquet1.ycor()
    racquet1.sety(y - 20)


# keyboard bindings
window.listen()
window.onkeypress(move_racquet1_up, "a")
window.onkeypress(move_racquet1_down, "d")


# movements of racquet2
def move_racquet2_up():
    y = racquet2.ycor()
    racquet2.sety(y + 20)


def move_racquet2_down():
    y = racquet2.ycor()
    racquet2.sety(y - 20)


# keyboard bindings
window.listen()
window.onkeypress(move_racquet2_up, "Up")
window.onkeypress(move_racquet2_down, "Down")

# ball movement


# game loop
while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("{} : {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("{} : {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if 340 < ball.xcor() < 350 and racquet2.ycor() + 40 > ball.ycor() > racquet2.ycor() - 40:
        ball.dx *= -1
    if -340 > ball.xcor() > -350 and racquet1.ycor() + 40 > ball.ycor() > racquet1.ycor() - 40:
        ball.dx *= -1
