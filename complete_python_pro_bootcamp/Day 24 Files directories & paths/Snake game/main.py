from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# 🦶🦶STEPS
    #1️⃣ Create a snake body
    #2️⃣ Move the snake
    #3️⃣ Control the snake
    #4️⃣ Detect collision with food
    #5️⃣ Create a scoreboard
    #6️⃣ Detect collision with wall
    #7️⃣ Detect collision with tail

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('🐸 Snake Game')
screen.tracer(0)

# CREATING THE SNAKE
snake = Snake()

# CREATING THE FOOD
food = Food()

# CREATING THE SCOREBOARD
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # MOVING THE STAKE
    snake.move()

    #DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        # print('nom, nom, nom')
        scoreboard.increase_score()

    #DETECT COLLISION WITH WALL 🔳
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()


    # DETECT COLLISION WITH TAIL 🐍
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()