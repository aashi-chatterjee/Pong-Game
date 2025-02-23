from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.speed("fastest")
        self.goto(x_cor, y_cor)

    def move_up(self):
        new_ycor = self.ycor() + 50
        self.goto(x=self.xcor(), y=new_ycor)

    def move_down(self):
        new_ycor = self.ycor() - 50
        self.goto(x=self.xcor(), y=new_ycor)
