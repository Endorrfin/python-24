import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'

turtle.addshape(image)
turtle.shape(image)

# def get_mouse_click_coordinate(x, y):
#     print('x', x, 'y', y)
# turtle.onscreenclick(get_mouse_click_coordinate)

# 🦶🦶STEPS
    #1️⃣ Convert the guess to Title case
    #2️⃣ Check if the guess is among the 50 states
    #3️⃣ Write correct guesses onto the map
    #4️⃣ Use a loop to allow the user to keep guessing
    #5️⃣ Record the correct guesses in a list
    #6️⃣ Keep track of the score


data = pandas.read_csv('50_states.csv')
# print('DATA', data)

all_states = data.state.to_list()
# print('ALL STATES', all_states)

guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                    prompt="What's another state's name?").title()
    # print('ANSWER STATE', answer_state)

    if answer_state == 'Exit':
        missing_state = [state for state in all_states if state not in guessed_states]
        print('MISSING STATE', missing_state)
        generate_missing_states = pandas.DataFrame(missing_state)
        generate_missing_states.to_csv('states_to_learn.csv')

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle() #hide turtle shape
        t.penup() #not drawing anything
        state_coordinate = data[data.state == answer_state]
        t.goto(state_coordinate.x.item(), state_coordinate.y.item())
        t.write(state_coordinate.state.item())
        # t.write(answer_state)




# keep screen open during the click
turtle.mainloop()

# screen.exitonclick()