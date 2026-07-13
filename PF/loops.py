# Write a program that takes a number n from the user and calculates the sum of all numbers from 1 to n.
# e.g. 1 + 2 + 3 + 4 + 5 = 15
"""
num = int(input("Enter a value:   "))
sum = 0
for x in range(1 , num + 1):
    sum += x
print(f"The sum of numbers till that value is: {sum}")
"""


# Take a number from the user and print its multiplication table from 1 to 10.
"""
table = int(input("Enter a value:   "))
x = 1
while x <= 10:
    ans = table * x
    print(f"{table} x {x} = {ans}")
    x += 1
"""


# Take an integer from the user and count how many digits it contains using a loop.
"""
number = int(input("Enter a value:   "))
count = 0
while number > 0:
        number = number // 10
        count += 1
print(count)
"""


# Take a number from the user and reverse its digits.
"""
num = abs(int(input("Enter a value:   ")))
integrate = 0
mod = 0
while num > 0:
    mod = num % 10
    num = num // 10
    integrate = (integrate * 10) + mod
print(integrate)
"""


# Print the right angle triangle pattern for a given number of rows
"""
num = int(input("Enter a Number"))
for x in range(1, num + 1):
    print("*" * x)
"""


