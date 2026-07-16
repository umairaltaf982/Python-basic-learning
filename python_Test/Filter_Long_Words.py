# Exercise 16 - Filter Long Words

# Write a function filter_long_words() that takes a list of words and an integer n and
# returns the list of words that are longer than n.

def filter_long_words(my_list, my_num):
    new_list = []
    for l in my_list:
        size = 0
        if l == "":
            return 0
        else:
            for n in l:
                size = size + 1
        temp = size
        if temp > my_num:
            new_list.append(l)
    return new_list

x = filter_long_words(["apple", "mango", "cat", "Elephant", "Lion"], 4)
print(x)