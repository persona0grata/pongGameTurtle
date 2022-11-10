import turtle as t
import random
playerAscore = 0
playerBscore = 0
ex_it = False

# create a window and declare a variable called window and call the screen()
window = t.Screen()
window.title("The Pong Game")
window.bgcolor("black")
window.setup(width=1000, height=750)
window.tracer(0)

box = t.Turtle()
box.shape("square")

# Creating the left paddle
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-450, 0)

# Creating the right paddle
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(450, 0)

# Code for creating the ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(5, 5)
ball_x_direction = 0.2
ball_y_direction = 0.2

# Code for creating pen for scorecard update
pen = t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.write("0 - SCORE - 0", align="center", font=('Monaco', 24, 'normal'))


# code for moving the leftpaddle
def leftpaddleup():
    y = leftpaddle.ycor()
    y = y + 30
    leftpaddle.sety(y)


def leftpaddledown():
    y = leftpaddle.ycor()
    y = y - 30
    leftpaddle.sety(y)


# code for moving the rightpaddle
def rightpaddleup():
    ry = rightpaddle.ycor()
    ry = ry + 30
    rightpaddle.sety(ry)


def rightpaddledown():
    ry = rightpaddle.ycor()
    ry = ry - 30
    rightpaddle.sety(ry)

def tapExit():
    ex_it = True




# Assign keys to play
window.listen()
window.onkeypress(leftpaddleup, 'w')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'Up')
window.onkeypress(rightpaddledown, 'Down')
window.onkeypress(tapExit, 'e')


while playerAscore != 11 and playerBscore != 11:
    while True:
        window.update()
        if playerAscore != 11 and playerBscore != 11:
            if (rightpaddle.ycor() + 40 > 365):
                rightpaddle.sety(325)

            if (rightpaddle.ycor() - 40 < -365):
                rightpaddle.sety(-325)

            if (leftpaddle.ycor() + 40 > 365):
                leftpaddle.sety(325)

            if (leftpaddle.ycor() - 40 < -365):
                leftpaddle.sety(-325)

                # moving the ball
            ball.setx(ball.xcor() + ball_x_direction * (random.randint(1, 4)))
            ball.sety(ball.ycor() + ball_y_direction)

            # border set up
            if ball.ycor() > 365:
                ball.sety(365)
                ball_y_direction *= -1
            if ball.ycor() < -365:
                ball.sety(-365)
                ball_y_direction *= -1

            if ball.xcor() > 490:
                ball.goto(0, 0)
                ball_x_direction *= -1
                playerAscore += 1
                pen.clear()
                pen.write("{} - SCORE - {} ".format(playerAscore, playerBscore),
                          align="center", font=('Monaco', 24, "normal"))
                rightpaddle.goto(450, 0)
                leftpaddle.goto(-450, 0)

            if (ball.xcor()) < -490:  # Left width paddle Border
                ball.goto(0, 0)
                ball_x_direction *= -1
                playerBscore += 1
                pen.clear()
                pen.write("{} - SCORE - {} ".format(playerAscore, playerBscore),
                          align="center", font=('Monaco', 24, "normal"))
                rightpaddle.goto(450, 0)
                leftpaddle.goto(-450, 0)

            # Handling the collisions with paddles.

            if (ball.xcor() > 440) and (ball.xcor() < 450) and (
                    ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40):
                ball.setx(440)
                ball_x_direction *= -1

            if (ball.xcor() < -440) and (ball.xcor() > -450) and (
                    ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
                ball.setx(-440)
                ball_x_direction *= -1

        else:
            break
window.clear()
while ex_it is False:
    window.bgcolor("black")

    pen = t.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()

    pen.goto(0, 0)

    if max(playerAscore, playerBscore) == playerAscore:
        pen.write("LEFT SIDE WINS!!!", align="center", font=('Monaco', 24, 'bold'))
        pen.goto(0, -100)
        pen.write("press E to exit", align="center", font=('Monaco', 19, 'normal'))
    else:
        pen.write("RIGHT SIDE WINS!!!", align="center", font=('Monaco', 24, 'bold'))
        pen.goto(0, -100)
        pen.write("press E to exit", align="center", font=('Monaco', 19, 'normal'))