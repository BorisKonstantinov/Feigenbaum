import sympy as sp
import time


# Define symbolic variable
x = sp.symbols('x')

# Define the formula symbolically
def myformula(x):
    return x + 5

# Get the symbolic expression of the formula


# Lambdify the symbolic expression to create a fast numeric function


def case_0(n):
    for _ in range(n):
        y = _ + 5
    return 0

def case_1(n):
    for _ in range(n):
        y = myformula(_)
    return 0

def case_2(n, formula=myformula):
    for _ in range(n):
        y = formula(_)  # Efficiently using the formula
    return 0

def race(n, repetitions):
    cases = [case_0, case_1, case_2]  # List of case functions
    start_time_case = [[0]*repetitions for _ in range(len(cases))]
    stop_time_case = [[0]*repetitions for _ in range(len(cases))]
    time_taken_case = [[0]*repetitions for _ in range(len(cases))]

    for case_index, case in enumerate(cases):
        for i in range(repetitions):
            start_time_case[case_index][i] = time.time()
            case(n)
            stop_time_case[case_index][i] = time.time()
            time_taken_case[case_index][i] = stop_time_case[case_index][i] - start_time_case[case_index][i]
        avg_time = sum(time_taken_case[case_index]) / repetitions
        print(f"Average time for {case}: {avg_time} seconds")


race(100000, 1000)
