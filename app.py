import streamlit as st
import random

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
    problem = f"{num1} ^ {num2} = ?"
    solution = num1 ** num2
    return problem, solution

def generate_math_problem():
    problem_types = [add_problem, subtract_problem, multiply_problem, square_problem]
    problem_type = random.choice(problem_types)
    return problem_type()

def get_answer(problem):
    answer = st.text_input(problem, '')
    if answer:
        return int(answer)

num_correct = 0

st.title('MindMath')

while True:
    problem, solution = generate_math_problem()
    answer = get_answer(problem)
    if answer == solution:
        num_correct += 1
        st.write('Correct!')
        break
    else:
        num_correct = 0
        st.write('Incorrect.')
