from turtle import Turtle, Screen
import random

is_race_on = False
new_turtle = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'pink', 'green', 'blue', 'purple', 'brown']
y_positions = [-150, -100, -50, 0, 50, 100, 150]
all_turtles = []

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner 🥇")
            else:
                print(f"You've lost 😡 The {winning_color} turtle is the winner")
            print(turtle.color())

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
