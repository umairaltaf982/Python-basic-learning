# Exercise 9 - Is a member
#
# Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a,
# and returns True if x is a member of a, False otherwise.
# (Note that this is exactly what the in operator does, but for the sake
# of the exercise you should pretend Python did not have this operator.)

def is_member(a, my_list):
    count = 0
    size = len(my_list)
    while size > 0:
        if my_list[count] == a:
            return True
        count = count + 1
        size = size - 1
    return False

x = is_member(17, [1,2,3,4,9])
print(x)

