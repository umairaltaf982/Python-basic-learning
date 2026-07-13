# Question 8 – Using name
# Create a decorator display_name.
# Before executing the function, print the function's name using:
# function.__name__
# Decorate a function named square().

def display_name(fx):
    def mfx():
        print("Function Name:", fx.__name__)
        fx()
    return mfx

@display_name
def square():
    print(5 * 5)

square()