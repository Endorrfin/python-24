import turtle
import pandas

screen = turtle.Screen()
screen.title('UA. Cities quiz')
image = 'blank_map_ua_cities.gif'

turtle.addshape(image)
turtle.shape(image)

# def get_mouse_click_coordinate(x, y):
#     # print('x', x, 'y', y)
# turtle.onscreenclick(get_mouse_click_coordinate)

# 🦶🦶STEPS
    #1️⃣ Convert the guess to Title case
    #2️⃣ Check if the guess is among the 50 states
    #3️⃣ Write correct guesses onto the map
    #4️⃣ Use a loop to allow the user to keep guessing
    #5️⃣ Record the correct guesses in a list
    #6️⃣ Keep track of the score


data = pandas.read_csv('25_ua_cities.csv', skipinitialspace=True)
# print('DATA', data)

# Create lists for both English and Ukrainian city names
all_cities_en = data.city_en.to_list()
all_cities_ua = data.city_ua.to_list()
print('ALL CITIES', all_cities_en, all_cities_ua)

# Create a dictionary to map any city name to its English version for data lookup
city_name_map = {}
for en, ua in zip(all_cities_en, all_cities_ua):
    city_name_map[en.lower()] = en  # Add 🇺🇸 name mapping
    city_name_map[ua.lower()] = en  # Add 🇺🇦 name mapping

guessed_cities = []

while len(guessed_cities) < 25:
    answer_cities = screen.textinput(title=f"{len(guessed_cities)} | 25 🌇 Cities ✅",
                                    prompt="What's another city name?").strip()
    # print('ANSWER STATE', answer_state)

    # Check for exit command
    if answer_cities.lower() == 'exit':
        missing_cities = []
        for city in all_cities_en:
            if city not in guessed_cities:
                missing_cities.append(city)
        print('MISSING CITIES', missing_cities)
        generate_missing_cities = pandas.DataFrame(missing_cities)
        generate_missing_cities.to_csv('cities_ua_to_learn.csv')
        break

    answer_city_lower = answer_cities.lower()

    if answer_city_lower in city_name_map:
        english_city_name = city_name_map[answer_city_lower]

        if english_city_name in guessed_cities:
            continue

        guessed_cities.append(english_city_name)
        t = turtle.Turtle()
        t.hideturtle() #hide turtle shape
        t.penup() #not drawing anything

        city_coordinate = data[data.city_en == english_city_name]
        t.goto(city_coordinate.x.item(), city_coordinate.y.item())
        t.write(answer_cities)

# keep screen open during the click
turtle.mainloop()

# screen.exitonclick()