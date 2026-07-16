# Exercise 23 - Spell Check

# Define a simple "spelling correction" function correct() that takes a string and sees to it that
# 1) two or more occurrences of the space character is compressed into one
# 2) inserts an extra space after a period if the period is directly followed by a letter.
# E.g. correct("This is very funny and cool.Indeed!") should return "This is very funny and cool. Indeed!"
# Tip: Use regular expressions!

import re


def correct(text):
    # 1) Compress two or more occurrences of the space character into one
    no_multi_spaces = re.sub(r' {2,}', ' ', text)

    # 2) Insert an extra space after a period if it is directly followed by a letter
    corrected_text = re.sub(r'\.(?=[A-Za-z])', '. ', no_multi_spaces)

    return corrected_text


# Example usage:
print(correct("This is very funny and cool.Indeed!"))
# Output: "This is very funny and cool. Indeed!"
