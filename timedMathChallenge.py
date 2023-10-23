#This program is to generate 10 random math problems for the user to solve.
#credits to @TechWithTim on YouTube for project idea and walkthrough
import random
import time

OPERATORS = ["+", "-", "*"] #operators to choose from when generating the problem
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


def generate_problem(): #generates the problem
    left = random.randint(MIN_OPERAND, MAX_OPERAND) #random number between 3 and 12
    right = random.randint(MIN_OPERAND, MAX_OPERAND) #random number between 3 and 12
    operator = random.choice(OPERATORS) #random operator
    #random.choice is going to randomly pick an element from a list

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr) #eval evalutes a string as if it was a python expression
    return expr, answer


wrong = 0
input("Press enter to start!")
print("----------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("----------------------")
print("Nice work! You finished in", total_time, "seconds!")
