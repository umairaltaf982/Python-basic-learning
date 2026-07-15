# Exercise 2 - Max of Three
# Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.

def max_of_three(a, b, c):
    if a > b and a > c:
        print(f"Maximum: {a}")

    elif b > a and b > c:
        print(f"Maximum: {b}")

    else:
        print(f"Maximum: {c}")

max_of_three(21, 24, 21)