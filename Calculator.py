from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("300x400")

expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)
def equalpress():
     global expression
     total = str(eval(expression))
     equation.set(total)
     expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")

equation = StringVar()
expression_field = Entry(root, textvariable=equation, font=('Arial', 16), bd=14, insertwidth=14, width=12)
expression_field.grid(row=0, column=0, columnspan=4)


buttons = ['7', '8', '9', '/','4', '5', '6', '*','1', '2', '3', '-','0', 'C', '=', '+']
row_val = 1
col_val = 0

for button in buttons:
    if button == 'C':
        Button(root, text=button, command=clear, height=2, width=5).grid(row=row_val, column=col_val)
    elif button == '=':
        Button(root, text=button, command=equalpress, height=2, width=5).grid(row=row_val, column=col_val)
    else:
        Button(root, text=button, command=lambda b=button: press(b), height=2, width=5).grid(row=row_val, column=col_val)

    col_val=col_val+1
    if col_val>3: 
        col_val=0
        row_val=row_val+1

root.mainloop()
