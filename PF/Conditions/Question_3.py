# Largest of Three Numbers
# Take three numbers from the user and print the largest one.
x = int(input("Enter first Number:   "))
y = int(input("Enter second Number:   "))
z = int(input("Enter third Number:   "))

if x > y and x > z:
    print(x)
if y > x and y > z:
    print(y)
if z > x and z > y:
    print(z)
