from tkinter import *
import math

def button_click(char):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + char)

def clear_display():
    entry.delete(0, END)

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, END)
        entry.insert(0, "Error")

def square_root():
    try:
        value = float(entry.get())
        if value >= 0:
            result = math.sqrt(value)
            entry.delete(0, END)
            entry.insert(0, str(result))
        else:
            entry.delete(0, END)
            entry.insert(0, "Error")
    except ValueError:
        entry.delete(0, END)
        entry.insert(0, "Error")

def percentage():
    try:
        value = float(entry.get())
        result = value / 100
        entry.delete(0, END)
        entry.insert(0, str(result))
    except ValueError:
        entry.delete(0, END)
        entry.insert(0, "Error")

def backspace():
    current = entry.get()[:-1]
    entry.delete(0, END)
    entry.insert(0, current)

root = Tk()
root.title("Calculator")

entry = Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("√", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("/", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("*", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3),
    ("C", 1, 0), ("<-", 1, 1), ("%", 1, 2), ("-", 1, 3)
]

for (text, row, column) in buttons:
    button = Button(root, text=text, padx=20, pady=20, command=lambda char=text: button_click(char))
    button.grid(row=row, column=column, padx=5, pady=5)

clear_button = Button(root, text="Clear", padx=20, pady=20, command=clear_display)
clear_button.grid(row=1, column=0, padx=5, pady=5)

calculate_button = Button(root, text="Calculate", padx=20, pady=20, command=calculate)
calculate_button.grid(row=5, column=2, padx=5, pady=5)

sqrt_button = Button(root, text="√", padx=20, pady=20, command=square_root)
sqrt_button.grid(row=2, column=3, padx=5, pady=5)

percentage_button = Button(root, text="%", padx=20, pady=20, command=percentage)
percentage_button.grid(row=1, column=2, padx=5, pady=5)

backspace_button = Button(root, text="<-", padx=20, pady=20, command=backspace)
backspace_button.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()
