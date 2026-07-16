# Exercise 21 - Char Frequency
#
# Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it.
# Represent the frequency listing as a Python dictionary. Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").

def char_freq(string):
    frequency = {}
    for char in string:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

test_string = "abbabcbdbabdbdbabababcbcbab"
print(char_freq(test_string))
