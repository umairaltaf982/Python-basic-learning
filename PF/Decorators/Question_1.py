# Question 1 – Basic Decorator
# Create a decorator named greet_decorator that prints:
# Starting function...
# before the decorated function executes and
# Function finished.
# after it finishes.
# Decorate a function say_hello() that prints:
# Hello, World!


def greet_decorator(fx):
    def mfx():
        print("Starting function...")
        fx()
        print("Function finished.")
    return mfx

@greet_decorator
def say_hello():
    print("Hello, World!")

say_hello()