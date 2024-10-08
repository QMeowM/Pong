import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("Pong Game")

screen.tracer(0)
paddle_l = Paddle((-380, 0))
paddle_r = Paddle((370, 0))
ball = Ball()
score = Score()
# screen.tracer(1)
"""We can use this to have the ball move continuously, 
but it's tricky to do gradual increase of speed"""

screen.listen()
screen.onkey(fun=paddle_r.move_up, key="Up")
screen.onkey(fun=paddle_r.move_down, key="Down")
screen.onkey(fun=paddle_l.move_up, key="w")
screen.onkey(fun=paddle_l.move_down, key="s")

game_on = True

while game_on:

    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.xcor() > 400:
        score.scoring("left")
        ball.reset()
        ball.speed(1)

    if ball.xcor() < -400:
        score.scoring("right")
        ball.reset()
        ball.speed(1)

    if 360 >= ball.xcor() >= 350 and ball.distance(paddle_r) <= 55:
        ball.bounce_on_paddle()
        score.scoring("right")

    if -370 <= ball.xcor() <= -360 and ball.distance(paddle_l) <= 55:
        ball.bounce_on_paddle()
        score.scoring("left")

screen.exitonclick()