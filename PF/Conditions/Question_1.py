# 1. Positive, Negative, or Zero
# Write a program that takes an integer from the user and prints:
# "Positive" if the number is greater than 0.
# "Negative" if the number is less than 0.
# "Zero" if the number is 0.

num = int(input("Enter an integer:   "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")