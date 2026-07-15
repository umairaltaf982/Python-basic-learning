# Exercise 6 - Sum and Multiply
#
# Define a function sum() and a function multiply() that sums and multiplies (respectively)
# all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10,
# and multiply([1, 2, 3, 4]) should return 24.

def new_sum(numbers):
    x = 0
    for i in numbers:
        x = i + x
    print(f"Sum = {x}")

def new_mult(numbers):
    x = 1
    for i in numbers:
        x = i * x
    print(f"Multiply = {x}")

new_sum([1, 2, 3, 4])
new_mult([1, 2, 3, 4])