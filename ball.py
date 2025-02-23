from turtle import Turtle
MOVE_DISTANCE = 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.moving_speed = 0.05

    def move(self):
        # move to top right corner
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_ycor)

    def bounce(self):
        self.y_move *= -1

    def has_been_hit(self):
        self.x_move *= -1
        self.moving_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.moving_speed = 0.05
        self.has_been_hit()
