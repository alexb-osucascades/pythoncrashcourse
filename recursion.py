


# What is recursion?

# Recursion is an algorithmic technique in which  function calls itself (either directly or indirectly) on a smaller problem of the same type to simplify the problem to a solvable state.

# (Bad) example


# If you run this, you'll get an error.

# def my_function():
#     my_function()

# This is recursive, but it causes an error because the function will continue to call itself and reach the maximum recursion depth

# In order to make a functional recursive function, we need to ensure that the function contains two cases:

# 1. Base Case
# Uses an if statement as an exit condition
# Creates an exit condition for our function
# Usually the most simple form of the problem

# 2. Recursive Case
# Runs if the base case's exit condition isn't met.
# Contains the actual recursive call (call to the function which contains it)


# Simple example:

def my_function(num):
    # This is the exit condition:
    if num > 100:
        # This is the base case
        print(num, "is higher than 100")
    else:
        # This it the recursive case
        print(num, "is less than 100")
        my_function(num*2) # recursive call to the same function

# calling the function from the outside
my_function(1)



# Problem 1: Factorial
def factorial(num):
    # change True to the exit condition
    if num <= 1:
        # change this to our base case
        return 1
    else:
        # change this to the recursive case
        return num * factorial(num - 1)


print("10! = ", factorial(10))
# the answer should be 3628800


# Problem 2: Fibonacci

def fibonacci(num):
    # change True to the exit condition
    if num <= 2:
        # change this to our base case
        return 1
    else:
        # change this to the recursive case
        return fibonacci(num - 1) + fibonacci(num - 2) 


print("fibonacci(10) = ",fibonacci(10))
# The answer should be 55



# We'll work on this one in class (if there's time)
def hanoi_move(start, end):
    return print (f"Move {start} To {end}")

def hanoi(num, start, through, end):
    # number of discs
    if num == 0:
        pass
    else:
        # recursive logic
        hanoi(num - 1, start, end, through)
        hanoi_move(start, end)
        hanoi(num - 1, through, start, end)

    return 

hanoi(4, "A", "B", "C")