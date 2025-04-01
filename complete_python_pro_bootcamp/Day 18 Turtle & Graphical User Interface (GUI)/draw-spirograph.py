import turtle as t
import random
from turtle import Screen

tim = t.Turtle()
t.colormode(255)

# Challenge - draw random walk using random colors
def random_color():
    r = random.randint(0, 255) #red
    g = random.randint(0, 255) #green
    b = random.randint(0, 255) #blue
    random_color = (r, g, b)
    return random_color

tim.speed("fastest")

# FIRST OPTION
# for _ in range(100):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.setheading(tim.heading() + 10)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()


# screen = Screen()
# screen.exitonclick()