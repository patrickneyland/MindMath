import streamlit as st
import random
import time

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

# def get_answer(problem):
#     answer = st.text_input(problem, '')
#     if answer:
#         return int(answer)

# num_correct = 0

# st.title("Mental Math Trainer")
# st.write("Welcome to MindMath, the app that helps you improve your mental math skills.")

# while True:
#     problem, solution = generate_math_problem()
#     answer = get_answer(problem)
#     if answer:
#         answer = int(answer)
#         if answer == solution:
#             num_correct += 1
#             st.write("Correct!")
#             break
#         else:
#             num_correct = 0
#             st.write("Incorrect.")
#             break
#     st.button("Submit")


# def check_answer(problem, answer):
#     _, solution = problem
#     if answer == solution:
#         return True
#     else:
#         return False

# num_correct = 0
# problem = generate_math_problem()

# while True:
#     st.write(problem[0])
#     answer = st.text_input("Your answer:", value='', key='answer_input')
#     if answer:
#         answer = int(answer)
#         if check_answer(problem, answer):
#             num_correct += 1
#             st.write("Correct!")
#         else:
#             num_correct = 0
#             st.write("Incorrect.")
#         problem = generate_math_problem()
#         st.write("New problem in 2 seconds...")
#         time.sleep(2)
#         st.write(problem[0])
#         st.text_input("Your answer:", value='', key='answer_input')

# st.write("# Welcome to MindMath!")
# st.write("Improve your mental math skills by answering the questions below.")

# with st.form(key='my_form'):
#     problem, solution = generate_math_problem()
#     user_answer = st.number_input("What is the answer to the following question?", problem)

#     if st.form_submit_button(label='Submit Answer'):
#         if int(user_answer) == solution:
#             num_correct += 1
#             st.write("Correct!")
#         else:
#             num_correct = 0
#             st.write("Incorrect.")
#         time.sleep(2)
#         problem, solution = generate_math_problem()
#         user_answer = st.number_input("What is the answer to the following question?", problem)
# with st.form("Math Trainer"):
#     st.header("Math Trainer")
#     problem, solution = generate_math_problem()
#     st.write(f"What is the solution to the problem: {problem}")
#     user_input = st.number_input(label='Your answer', step=1)
#     submitted = st.form_submit_button("Submit")
#     if submitted:
#         if user_input == solution:
#             num_correct += 1
#             st.write("Correct!")
#             time.sleep(2)
#             problem, solution = generate_math_problem()
#         else:
#             num_correct = 0
#             st.write("Incorrect.")
#     st.write(f"Number of correct answers: {num_correct}")

st.title("MindMath")

# with st.form("math_form"):
#     problem, solution = generate_math_problem()
#     st.write(problem)
#     user_input = st.number_input("Enter your answer", step=1)
#     if st.form_submit_button("Submit"):
#         if user_input == solution:
#             st.write("Correct!")
#         else:
#             st.write("Incorrect.")
#         time.sleep(2)
#     else:
#         st.write(" ")

problem, solution = generate_math_problem()
st.write(problem)

form = st.form(key="math_form")
user_input = form.number_input("Enter your answer", step=1)
submit_button = form.form_submit_button("Submit")

if submit_button:
    if user_input == solution:
        st.write("Correct!")
    else:
        st.write("Incorrect.")
    time.sleep(2)
else:
    st.write(" ")