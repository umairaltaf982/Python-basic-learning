# Question 2 – Decorator that Modifies Output
# Create a decorator called stars that prints:
# ***************
# before and after the decorated function.
# Decorate a function welcome() that prints:
# Welcome to Python!

def stars(fx):
    def mfx():
        print("*************************")
        fx()
        print("**************************")
    return mfx

@stars
def welcome():
    print("Welcome to Python")


welcome()