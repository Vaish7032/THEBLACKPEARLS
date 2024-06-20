from tkinter import *
import math

# Global variables for memory function
memory = 0
expression = ""

# Function to update the input field when a button is pressed
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except ZeroDivisionError:
        equation.set("Cannot divide by zero")
        expression = ""
    except Exception:
        equation.set("Invalid input")
        expression = ""

# Function to clear the input field
def clear():
    global expression
    expression = ""
    equation.set("")

# Function to calculate square root
def sqrt():
    try:
        global expression
        total = str(math.sqrt(float(expression)))
        equation.set(total)
        expression = ""
    except ValueError:
        equation.set("Invalid input")
        expression = ""

# Function to calculate exponentiation
def power():
    global expression
    expression += ""
    equation.set(expression)

# Function to add to memory
def mem_add():
    global memory, expression
    memory += float(equation.get())
    expression = ""
    equation.set("")

# Function to recall memory
def mem_recall():
    global memory
    equation.set(memory)
    expression = str(memory)

# Function to clear memory
def mem_clear():
    global memory
    memory = 0

# Creating the main window
gui = Tk()
gui.title("Calculator")
gui.configure(bg="#333333")

equation = StringVar()

# Create the input field
input_field = Entry(gui, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4, bg="#ffffff")
input_field.grid(row=0, column=0, columnspan=4)

# Define button styles
button_font = ('Arial', 18)
button_bg = "#4CAF50"
button_fg = "#ffffff"

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('√', 5, 0), ('^', 5, 1), ('.', 5, 2), ('M+', 5, 3),
    ('MR', 6, 0), ('MC', 6, 1)
]

# Function to handle button clicks
def on_click(value):
    if value == '=':
        equalpress()
    elif value == 'C':
        clear()
    elif value == '√':
        sqrt()
    elif value == '^':
        power()
    elif value == 'M+':
        mem_add()
    elif value == 'MR':
        mem_recall()
    elif value == 'MC':
        mem_clear()
    else:
        press(value)

# Create buttons
for (text, row, col) in buttons:
    Button(gui, text=text, font=button_font, bg=button_bg, fg=button_fg, command=lambda text=text: on_click(text), height=2, width=6).grid(row=row, column=col, padx=5, pady=5)

# Start the GUI
gui.mainloop()
