# Reverse a Number (While Loop)
# Take an integer and print its reverse.

num = abs(int(input("Enter a value:   ")))
integrate = 0
mod = 0
while num > 0:
    mod = num % 10
    num = num // 10
    integrate = (integrate * 10) + mod
print(integrate)