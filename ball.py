from turtle import Turtle

i = 1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        # self.speed(1)
        self.setheading(45)
        self.new_x = 10
        self.new_y = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.new_x
        new_y = self.ycor() + self.new_y
        self.goto(new_x, new_y)
        if self.ycor() <= -280 or self.ycor() >= 280:
            self.new_y *= -1

    def bounce_on_paddle(self):
        self.new_x *= -1
        self.ball_speed *= 0.9

    def reset(self):
        self.hideturtle()
        self.home()
        self.showturtle()
        self.new_x *= -1
        self.new_y = self.new_x
        self.ball_speed = 0.1