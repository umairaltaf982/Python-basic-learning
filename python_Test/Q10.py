# Exercise 10 - Overlapping
#
# Define a function overlapping() that takes two lists and
# returns True if they have at least one member in common, False otherwise.
# You may use your is_member() function, or the in operator,
# but for the sake of the exercise, you should (also) write it using two nested for-loops.

def overlapping(list1, list2):
    size1 = len(list1)
    size2 = len(list2)
    for l1 in list1:
        for l2 in list2:
            if l1 == l2:
                return True
    return False

x = overlapping([1, 2, 3, 4], [4, 5, 6, 7])
print(x)

y = overlapping([1, 2, 3, 4], [7, 5, 6, 0])
print(y)