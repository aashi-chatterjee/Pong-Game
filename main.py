from turtle import Screen
import time

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()

screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # to detect collision w/wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()


    # to detect collision w/paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.has_been_hit()

    # to detect r paddle missing the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # to detect l paddle missing the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
