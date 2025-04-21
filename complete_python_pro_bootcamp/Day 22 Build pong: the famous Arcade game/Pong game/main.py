from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# 🦶🦶STEPS
    #1️⃣ Create the screen
    #2️⃣ Create & move a paddle
    #3️⃣ Create another paddle
    #4️⃣ Create the ball & make it move
    #5️⃣ Detect collision with wall & bounce
    #6️⃣ Detect collision with paddle
    #7️⃣ Detect when paddle misses
    #8️⃣ Keep score

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('🏓 Pong')
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, 'Up')
screen.onkey(right_paddle.go_down, 'Down')
screen.onkey(left_paddle.go_up, 'w')
screen.onkey(left_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #DETECT COLLISION WITH WALL
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()

    #DETECT COLLISION WITH R_PADDLE
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        print('Made contact')

    #DETECT RIGHT PADDLE MISSES
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    #DETECT LEFT PADDLE MISSES
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()



