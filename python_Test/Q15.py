# Exercise 15 - Longest Word

# Write a function find_longest_word() that takes a list of words and returns the length of the longest one.

def find_longest_word(my_list):
    maximum = 0
    for l in my_list:
        size = 0
        if l == "":
            return 0
        else:
            for n in l:
                size = size + 1
        temp = size
        if temp > maximum:
            maximum = temp
    return maximum


x = find_longest_word(["apple", "mango", "cat", "Elephant", "Lion"])
print(x)