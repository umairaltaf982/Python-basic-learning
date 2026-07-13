# Question 3 – Decorator with Function Arguments
# Create a decorator log_call that prints:
# Calling function...
# before executing the function.
# Decorate a function:
# add(a, b)
# that returns the sum of two numbers.


def log_call(fx):
    def mfx(a, b):
        print("Calling function...")
        fx(a, b)
    return mfx

@log_call
def addition(a, b):
    print(f"The addition value is: {a + b}")

addition(4, 5)