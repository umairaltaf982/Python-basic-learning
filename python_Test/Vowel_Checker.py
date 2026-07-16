# Exercise 4 - Vowel Checker
# Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise

def check_vowel(alphabet):
    if len(alphabet) == 1:
        if alphabet in "aeiouAEIOU":
            return True
        else:
            return False

    else:
        print(f"Invalid character: {alphabet}")
        return False

x = check_vowel("I")
y = check_vowel("x")
print(x)
print(y)