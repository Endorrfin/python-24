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

directions = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fastest")

for _ in range(360):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()