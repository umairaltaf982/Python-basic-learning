# Exercise 8 - Is a Palindrome
#
# Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards).
# For example, is_palindrome("radar") should return True.

def is_palindrome(word):
    reversed_text = ""
    for char in word:
        reversed_text = char + reversed_text
    if word == reversed_text:
        return True
    else:
        return False

x = is_palindrome("radar")
y = is_palindrome("book")
print(x)
print(y)
