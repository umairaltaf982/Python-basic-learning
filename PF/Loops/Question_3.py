# Take a number from the user and print its multiplication table from 1 to 10.

table = int(input("Enter a value:   "))
x = 1
while x <= 10:
    ans = table * x
    print(f"{table} x {x} = {ans}")
    x += 1
