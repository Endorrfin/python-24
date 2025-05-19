from tkinter import *

def convert():
    # Get the input value
    value = float(distance_input.get())

    # Check which conversion mode is selected
    if conversion_mode.get() == 'miles_to_km':
        # Miles to kilometers conversion
        result = round(value * 1.609)
        result_label.config(text=f"{result}")
        unit_label.config(text='Km')
        input_unit_label.config(text="Miles")
    else:
        # Kilometers to miles
        result = round(value / 1.609, 2)
        result_label.config(text=f"{result}")
        unit_label.config(text='Miles')
        input_unit_label.config(text='Km')


window = Tk()
window.title('Distance converter')
window.config(padx=10, pady=10)

# Variable to store the conversion mode
conversion_mode = StringVar()
conversion_mode.set('miles_to_km') #Default mode

# Radio buttons for conversion mode selection
miles_to_km_radio = Radiobutton(
    text='Miles to Kilometers',
    variable=conversion_mode,
    value='miles_to_km',
    command=lambda: convert() if distance_input.get() else None
)
miles_to_km_radio.grid(column=1, row=0, sticky='w')

km_to_miles_radio = Radiobutton(
    text="Kilometers to Miles",
    variable=conversion_mode,
    value="km_to_miles",
    command=lambda: convert() if distance_input.get() else None
)
km_to_miles_radio.grid(column=1, row=1, sticky="w")

# Input field
distance_input = Entry(width=10)
distance_input.grid(column=1, row=3)

# Labels
input_unit_label = Label(text="Miles")  # Initially set to Miles
input_unit_label.grid(column=2, row=3)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=4)

result_label = Label(text="0")
result_label.grid(column=1, row=4)

unit_label = Label(text="Km")  # Initially set to Km
unit_label.grid(column=2, row=4)

# Button to calculate
calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=5, pady=10)





window.mainloop()