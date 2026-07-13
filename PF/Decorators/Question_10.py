# Question 10 – Combined Practice
# Create a decorator named debug.
# Before executing any function, print:
# Function Name
# Function Docstring
# Positional Arguments
# Keyword Arguments
# Decorate:
# calculate_total(price, tax=0.18)
# Call it using both positional and keyword arguments.


def debug(fx):
    def mfx(*args, **kwargs):
        print("Function Name:", fx.__name__)
        print("Function Docstring:", fx.__doc__)
        print("Arguments:", args)
        print("Keyword Arguments:", kwargs)
        return fx(*args, **kwargs)
    return mfx

@debug
def calculate_total(price, tax=0.18):
    total = price + (price * tax)
    print("Total:", total)


calculate_total(1000, 20)

