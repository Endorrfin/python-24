from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# JSON
# Write: json.dump()
# Read: json.load()
# Update: json.update()

# 🦶🦶STEPS
    #1️⃣ Add a "Search" button next to the website entry field
    #2️⃣ Adjust the layout and the other widgets as needed to get the desired look
    #3️⃣ Create function called find_password() that gets triggered when the "Search" button is pressed
    #4️⃣ Check if the user's text entry matches an item in the data.json
    #5️⃣ If yes, show a messagebox with the website's name and password
    #6️⃣ Catch an exception that might occur trying to access the data.json showing a messagebox with the text: 'No Data File Found'
    #7️⃣ If the user's website does not exist inside the data.json, show a messagebox that reads 'No details for the website exists'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    # print(f"You password is {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='🙊 Oops', message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open('data.json', 'r') as data_file:
                # READ DATA
                # Reading old data
                data = json.load(data_file)
                # print('🔹 TYPE', type(data), 'DATA', data)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                # WRITE DATA
                json.dump(new_data, data_file, indent=4)
        else:
            # UPDATE DATA
            # Updating old data with new data
            data.update(new_data)

            with open('data.json', 'w') as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
            print('ℹ️ DATA', data)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='⛔️ No Data File Found.')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f'📧 Email: {email}\n🤫 Password: {password}')
        else:
            messagebox.showinfo(title='Error', message=f"🙅‍♂️ No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password manager')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# LABELS
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# ENTRIES
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'lkirnadz@gmail.com')
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# BUTTONS
search_button = Button(text='Search', width=13, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text='Generate password', command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text='➕', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()