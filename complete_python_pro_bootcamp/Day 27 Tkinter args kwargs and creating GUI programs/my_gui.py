# from tkinter import Tk, Label, Button
from tkinter import *

# 📝 TKINTER
## PACK
    # 1. Side: parameter determines the direction of the widgets in the layout
        # 1.1. 'top'
        # 1.2. 'bottom'
        # 1.3. 'left'
        # 1.4. 'right'
    # 2. Expand: determines whether the widget should expand to occupy any extra spaces allocated to the container
        # 2.1. expand=True
        # 2.2. expand=False
    # 3. Fill: determines if a widget will occupy the available space
        # 3.1. 'none'
        # 3.2. 'x'
        # 3.3. 'y'
        # 3.4. 'both'
    # 4. ipadx, ipady: parameters create internal paddings for widgets
        # 4.1. ipadx=40
        # 4.2. ipady=80
    # 5. padx, pady: parameters allow you to specify padding to be added horizontally and vertically, respectively
        # 5.1 pady=10
        # 5.2 padx=10
    # 6. Anchor: parameter allows you to anchor the widget to the edge of the allocated space
        # 6.1. ‘n’	North or Top Center
        # 6.2. ‘s’	South or Bottom Center
        # 6.3. ‘e’	East or Right Center
        # 6.4. ‘w’	West or Left Center
        # 6.5. ‘nw’	North West or Top Left
        # 6.6. ‘ne’	North East or Top Right
        # 6.7. ‘se’	South East or Bottom Right
        # 6.8. ‘sw’	South West or Bottom Left
        # 6.9. ‘center’	Center

## GRID: learn how to use the grid geometry manager to place widgets on a container


## PLACE: show how to use the place geometry manager to precisely position widgets within its container using the (x, y) coordinate system
        # place(x=20, y=70)



window = Tk()
window.title('My first GUI Program')
window.minsize(width=600, height=400)

# LABEL
my_label = Label(text="I Am a Label", font=('Calibre', 24, 'bold'))
my_label.pack(side='top')


my_label['text'] = 'My Title'
my_label.config(text='New Text')

# BUTTON
def button_clicked():
    print('I got clicked 💥')
    new_text = input.get()
    # my_label.config(text='Button Got Clicked')
    my_label.config(text=new_text)

button = Button(text='Click me', command=button_clicked)
button.pack()

# ENTRY
input = Entry(width=18)
input.pack()
print(input.get())

# TEXT
text = Text(height=5, width=30)
# Puts cursor in texbox.
text.focus()
# Adds some text to begin with.
text.insert(END, 'Example of multi-line text entry.')
# Get's current value in textbox at line 1, character 0
print(text.get('1.0', END))
text.pack()

# SPINBOX
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# SCALE
# Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


#CHECKBUTOON
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text='Is On?', variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# RADIOBUTTON
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton3 = Radiobutton(text="Option3", value=3, variable=radio_state, command=radio_used)
radiobutton4 = Radiobutton(text="Option4", value=4, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()
radiobutton4.pack()


#LISTBOX
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana", "Lemon", "Kiwi"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()













window.mainloop()