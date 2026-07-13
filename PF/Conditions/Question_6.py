# Take three sides of a triangle.
# Check:
# Whether a triangle can be formed.
# If yes, print:
# Equilateral
# Isosceles
# Scalene

x = int(input("Enter first Side:   "))
y = int(input("Enter second Side:   "))
z = int(input("Enter third Side:   "))

if x == y == z:
    print("Equilateral Triangle")
elif x == y != z or x != y == z or x == z != y:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")