import random
import tkinter as tk
import tkinter.font as tkFont

def add_problem():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    problem = f"{num1} + {num2} = ?"
    solution = num1 + num2
    return problem, solution

def subtract_problem():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    problem = f"{num1} - {num2} = ?"
    solution = num1 - num2
    return problem, solution

def multiply_problem():
    num1 = random.randint(1, 15)
    num2 = random.randint(1, 15)
    problem = f"{num1} * {num2} = ?"
    solution = num1 * num2
    return problem, solution

def square_problem():
    num1 = random.randint(1, 10)
    num2 = random.randint(0, 4)
    problem = f"{num1}^{num2} = ?"
    solution = num1 ** num2
    return problem, solution

def generate_math_problem():
    problem_types = [add_problem, 
                     subtract_problem, 
                     multiply_problem,  
                     square_problem]
    problem_type = random.choice(problem_types)
    return problem_type()

def check_answer():
    global num_correct, solution
    answer = int(entry.get())
    if answer == solution:
        num_correct += 1
        result_label.configure(text="Correct!")
    else:
        num_correct = 0
        result_label.configure(text=f"Incorrect. The answer was {solution}")
    entry.delete(0, tk.END)
    problem, solution = generate_math_problem()
    problem_label.configure(text=problem)

num_correct = 0
solution = None

root = tk.Tk()
root.geometry("400x300")
root.title("Math Quiz")
font = tkFont.Font(size=20)

problem, solution = generate_math_problem()

problem_label = tk.Label(root, text=problem, font=font)
problem_label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Check", command=check_answer)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()