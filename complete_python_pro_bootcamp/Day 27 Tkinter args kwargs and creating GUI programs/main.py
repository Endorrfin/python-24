# import tkinter
import tkinter
from tkinter import Tk, Label, Button
import turtle

window = tkinter.Tk()
window.title('My first GUI Program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=10)

def button_clicked():
    print('I got clicked 💥')
    new_text = input.get()
    my_label.config(text=new_text)

# Label
my_label = tkinter.Label(text="I Am a Label", font=('Calibre', 24, 'bold'))
my_label.config(text='New Text')
my_label.pack(side='top')
# pack
# my_label.pack(slice='left')
# my_label.place(x=30, y=80)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=30)


#Button
button = Button(text='Click me', command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text='New Button')
new_button.grid(column=2, row=0)

#Entry
input = tkinter.Entry(width=10)
print(input.get())
input.grid(column=2, row=2)


# tim = turtle.Turtle()
# tim.write('Some text', font=('Times New Roman', 80, 'bold'))


window.mainloop()