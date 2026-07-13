# Question 4 – Decorator Using *args
# Write a decorator named before_after.
# The decorator should work for any number of positional arguments using *args.
# Decorate a function multiply(a, b, c) that returns the product of three numbers.

def before_after(fx):
    def mfx(*args):
        print("Before Function")
        result = fx(*args)
        print("After Function")
        return result
    return mfx

@before_after
def multiply(a, b, c):
    return a*b*c

print(multiply(34,2,1))