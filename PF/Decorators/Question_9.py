# Question 9 – Using doc
# Write a function with the following docstring:
# Returns the cube of a number.
# Create a decorator that prints the function's docstring before calling the function.


def show_doc(fx):
    def mfx():
        print(fx.__doc__)
        fx()
    return mfx

@show_doc
def cube():
    print(3 ** 3)

cube()