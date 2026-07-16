# Exercise 13 - Max in List

# The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two
# and three numbers, respectively. But suppose we have a much larger number of numbers,
# or suppose we cannot tell in advance how many they are?
# Write a function max_in_list() that takes a list of numbers and returns the largest one.

def max_in_list(my_list):
    maximum = 0
    for n in my_list:
        if n > maximum:
            maximum = n
    return maximum

x = max_in_list([21, 19, 17, 22, 21, 18, 16, 10])
print(x)