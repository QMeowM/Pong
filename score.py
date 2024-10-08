from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        # self.goto(0, -400)
        # self.pensize(20)
        # self.pencolor("white")
        # self.pendown()
        # self.goto(0,400)
        # self.penup()
        self.goto(0, 200)
        self.l_score = 0
        self.r_score = 0
        self.scoring("start")



    def scoring(self, side):
        if side == "left":
            self.l_score += 1
        if side == "right":
            self.r_score += 1
        self.clear()
        self.write(align="center", font=("Courier", 80, "italic"), arg=f"{self.l_score} : {self.r_score}")





