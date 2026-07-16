# Exercise 12 - Histograms

# Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
# For example, histogram([4, 9, 7]) should print the following:

# xxxx
# xxxxxxxxx
# xxxxxxx

def histogram(my_list):
    for n in my_list:
        x = ""
        while n > 0:
            x = x + "x"
            n = n - 1
        print(x)

histogram([4, 9, 7])