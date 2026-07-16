# Exercise 14 - Words into Integers
from operator import index


# Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.

def words_into_len(my_list):
    new_list = []
    for l in my_list:
        size = 0
        if l == "":
            print("0")
        else:
            for n in l:
                size = size + 1
        new_list.append(size)
    print(new_list)

words_into_len(["apple", "mango", "cat", "Lion"])