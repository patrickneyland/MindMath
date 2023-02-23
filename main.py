import random
import tkinter as tk
import tkinter.font as tkFont
from customtkinter import *


def add_problem():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    problem = f"{num1} + {num2}"
    solution = num1 + num2
    return problem, solution


def subtract_problem():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    problem = f"{num1} - {num2}"
    solution = num1 - num2
    return problem, solution


def multiply_problem():
    num1 = random.randint(1, 15)
    num2 = random.randint(1, 15)
    problem = f"{num1} * {num2}"
    solution = num1 * num2
    return problem, solution


def square_problem():
    num1 = random.randint(1, 10)
    num2 = random.randint(0, 4)
    problem = f"{num1}^{num2}"
    solution = num1 ** num2
    return problem, solution


def generate_math_problem():
    problem_types = []
    if var_add.get():
        problem_types.append(add_problem)
    if var_sub.get():
        problem_types.append(subtract_problem)
    if var_mul.get():
        problem_types.append(multiply_problem)
    if var_squ.get():
        problem_types.append(square_problem)
    problem_type = random.choice(problem_types)
    return problem_type()


def check_answer(event):
    global num_correct, solution
    answer = int(entry.get())
    if answer == solution:
        num_correct += 1
        entry.configure(text_color='green')
        #result_label.configure(text="Correct!")
    else:
        num_correct = 0
        entry.configure(text_color='red')
        #result_label.configure(text=f"Incorrect. The answer was {solution}")
    entry.after(500, lambda: entry.delete(0, tk.END))
    entry.after(500, lambda: entry.configure(text_color='gray'))
    problem, solution = generate_math_problem()
    problem_label.configure(text=problem)


def check_question(*args):
    if '?' in var_entry.get():
        var_entry.set(var_entry.get().replace('?', ''))
    elif not var_entry.get():
        var_entry.set('?')


num_correct = 0
solution = None

root = CTk()
window = CTkToplevel()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size and position
window_width = 800
window_height = 600
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))


root.title("Math Quiz")
font = CTkFont(size=60)
var_add = IntVar(value=1)
var_sub = IntVar(value=1)
var_mul = IntVar(value=1)
var_squ = IntVar(value=1)
problem, solution = generate_math_problem()

frame = CTkFrame(root, fg_color='#242424')
frame.pack(expand=True, fill='both')
frame.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure((0,1), weight=1)
problem_label = CTkLabel(frame, text=problem, font=font, anchor='e')
problem_label.grid(row=0, column=0, sticky='S')
var_entry = StringVar(value='?')
entry = CTkEntry(frame, font=font, fg_color='#242424', border_width=0, text_color='gray', textvariable=var_entry, justify='right', insertontime=0)
entry.after(100, entry.focus_set)
var_entry.trace_add('write', check_question)
entry.grid(row=1, column=0, sticky='N')

root.bind('<Return>', check_answer)
#button = CTkButton(root, text="Check", command=check_answer)
#button.pack()

#result_label = CTkLabel(root, text="")
#result_label.pack()

frame = CTkFrame(window)
frame.pack(side='bottom',  fill='x')
frame.grid_columnconfigure((0,1,2,3), weight=1)
add_checkbox = CTkCheckBox(frame, text="Addition", variable=var_add, onvalue=1, offvalue=0)
add_checkbox.grid(row=0, column=0, padx=20, pady=10)
var_sub = IntVar(value=1)
sub_checkbox = CTkCheckBox(frame, text="Substraction", variable=var_sub, onvalue=1, offvalue=0)
sub_checkbox.grid(row=0, column=1, padx=20, pady=10)
var_mul = IntVar(value=1)
mul_checkbox = CTkCheckBox(frame, text="Multiplication", variable=var_mul, onvalue=1, offvalue=0)
mul_checkbox.grid(row=0, column=2, padx=20, pady=10)
var_squ = IntVar(value=1)
squ_checkbox = CTkCheckBox(frame, text="Square", variable=var_squ, onvalue=1, offvalue=0)
squ_checkbox.grid(row=0, column=3, padx=20, pady=10)
root.mainloop()