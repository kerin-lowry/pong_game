from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

RIGHT_PADDLE_POS = 350
LEFT_PADDLE_POS = -350

#screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game - Kerin Lowry")
screen.tracer(0)

#create paddles
right_paddle = Paddle(RIGHT_PADDLE_POS)
left_paddle = Paddle(LEFT_PADDLE_POS)

#create ball
ball = Ball()

#create score
score = Score()

#wait for screen events
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_down, "s")

#game loop
game_on = True
while game_on:
    screen.update()
    ball.move()
    #check collision with top walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    #check collison with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        #ball.speed_up()
    #check if a player misses the ball
    if ball.xcor() > 380:
        #update player A score with an extra point
        score.update_score("left")
        ball.recenter()
    if ball.xcor() < -380:
        #update player B score with an extra point
        score.update_score("right")
        ball.recenter()


screen.exitonclick()