import turtle
import pandas
import tkinter as tk

screen = turtle.Screen()
screen.title('UA. Cities quiz')
image = 'blank_map_ua_cities.gif'
screen.setup(960, 720)

# Get the underlying Tkinter canvas and root window
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()

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

# Create custom input widgets in the top-left corner
input_frame = tk.Frame(root, bg='#333333', padx=10, pady=10)
input_frame.place(x=10, y=580)  # Position in the Down-left

# Create label for showing progress
counter_label = tk.Label(input_frame, text="C I T I E S : 0/25", fg="white", bg="#333333", font=("Arial", 12, "bold"))
counter_label.pack(pady=(0, 5))

# Create entry field
entry_var = tk.StringVar()
entry = tk.Entry(input_frame, textvariable=entry_var, width=25, font=("Arial", 11))
entry.pack(pady=(0, 5))

# Function to process the guess
def process_guess():
    answer_cities = entry_var.get().strip()
    entry_var.set("")  # Clear the entry field

    # Check for exit command
    if answer_cities.lower() == 'exit':
        missing_cities = []
        for city in all_cities_en:
            if city not in guessed_cities:
                missing_cities.append(city)
                print('MISSING CITIES', missing_cities)
                generate_missing_cities = pandas.DataFrame(missing_cities)
                generate_missing_cities.to_csv('cities_ua_to_learn.csv')
                return
    answer_city_lower = answer_cities.lower()

    if answer_city_lower in city_name_map:
        english_city_name = city_name_map[answer_city_lower]

        if english_city_name in guessed_cities:
            return

        guessed_cities.append(english_city_name)
        counter_label.config(text=f"Cities: {len(guessed_cities)}/25")

        # Create shadow effect
        shadow = turtle.Turtle()
        shadow.hideturtle()
        shadow.penup()

        # Get city coordinates
        city_coordinate = data[data.city_en == english_city_name]
        city_x = city_coordinate.x.item()
        city_y = city_coordinate.y.item()

        # Draw shadow text
        shadow.color('black')
        shadow.goto(city_x + 2, city_y - 2)
        shadow.write(answer_cities, align="center", font=("Arial", 12, "bold"))

        # Draw main text
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color('white')
        t.goto(city_x, city_y)
        t.write(answer_cities, align="center", font=("Arial", 12, "bold"))

# Create a submit button
submit_button = tk.Button(input_frame, text="Submit", command=process_guess, bg="#4a90e2", fg="Darkgreen", font=("Arial", 12, "bold"))
submit_button.pack(fill="x")

# Bind Enter key to submit button
entry.bind("<Return>", lambda event: process_guess())
entry.focus()  # Set focus to the entry field

screen.tracer(0)  # Turn off automatic updates
turtle.mainloop() # Force screen update after drawing


