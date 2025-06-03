import tkinter as tk
from tkinter import messagebox

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculate(expression):
    try:
        result = eval(expression)
        return f"{result:.2f}"
    except Exception:
        messagebox.showerror("Zero Error", "Cannot be divided by zero")
        return ""

def press(button_text):
    global reset_next
    if reset_next:
        entry.delete(0, tk.END)
        reset_next = False

    entry.insert(tk.END, button_text)

def evaluate():
    global reset_next
    exp = entry.get()
    result = calculate(exp)
    entry.delete(0, tk.END)
    if result is not None:
        entry.insert(tk.END, result)

    reset_next = True  

def clear():
    global reset_next
    entry.delete(0, tk.END)
    reset_next = False

window = tk.Tk()
window.title("Calculator")
window.geometry("375x415")
window.resizable(False, False)

entry = tk.Entry(window, width=20, font=('Arial', 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, ipady=10)

reset_next = False  

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(window, text=text, width=5, height=2, font=('Arial', 18), command=evaluate)
    elif text == "C":
        button = tk.Button(window, text=text, width=5, height=2, font=('Arial', 18), command=clear)
    else:
        button = tk.Button(window, text=text, width=5, height=2, font=('Arial', 18), command=lambda key=text: press(key))
    
    button.grid(row=row, column=col, padx=5, pady=5)
   
window.mainloop()