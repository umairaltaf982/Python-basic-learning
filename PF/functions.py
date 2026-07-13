"""
def my_func():
    print("Hello World")
my_func()
"""
import operator
from email import message

# Temperature Calculation
"""
def temp_calc(fehr):
    return (fehr - 32) * 5 / 9

temp = temp_calc(212)
print(temp)
print(temp_calc(102))
"""

# Python Arguments
"""
def name_age(name, age):
    print(f"My name is {name}, I am " , age)

name_age("Umair", 23)
"""


# Default Parameters
"""
def country_name(name = "Lithuania"):
    message = f"My country name is {name}"
    return message

message = country_name("Australia")
print(message)
message = country_name()
print(message)
"""


# Custom Calculator
# Create a function:
# calculator(operation, *args)
# where:
# "add" → add all numbers
# "multiply" → multiply all numbers
# "max" → return maximum number
"""
def calculator(operation, *args):
    oper = 0
    if operation == "add":
        oper = sum(args)
    if operation == "multiply":
        oper = 1
        for n in args:
            oper = oper * n
    if operation == "max":
        oper = max(args)
    print(f"{operation} of values is : {oper}")

calculator("add", 23 , 34, 32, 12)
calculator("multiply", 23 , 34, 32, 12)
calculator("max", 23 , 34, 32, 12)
"""


# Write a function:
# employee(id, **kwargs)
# that stores and displays employee information dynamically.
# Example:
# employee(101, name="Ali", department="IT", salary=50000)
"""
def employee(id, **kwargs):
    print(f"Employee ID: {id}")
    if not kwargs:
        print("No additional information!!!")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

employee(101, name="Ali", department="IT", salary=50000)
employee(102, name="Sara", role="Manager", project="Alpha", remote=True)
employee(103)
"""


# Create a function:
# shopping_cart(*items, **details)
# that displays all items purchased and customer details.
"""
def shopping_cart(*items, **details):
    count = 0
    for i in items:
        count = count + 1
        print(f"Product {count} is: {i}")
    for key, value in details.items():
        print(f"{key} : {value}")

shopping_cart(
    "Milk",
    "Bread",
    "Eggs",
    customer="Umair",
    city="Sargodha"
)
"""

# Wrapper Function
"""
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

def wrapper(*args, **kwargs):
    print("[LOG]: Arguments received! Forwarding them now...")
    greet(*args, **kwargs)

wrapper("Ali", 22)
"""


