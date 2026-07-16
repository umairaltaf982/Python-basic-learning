# Exercise 3 - Length of String
# Define a function that computes the length of a given list or string.

def length(string):
    size = 0
    if string == "":
        print(size)

    else:
        for n in string:
            size = size + 1
    print(size)

length("My Name is Umair")