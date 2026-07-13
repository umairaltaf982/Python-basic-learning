# Number Pyramid (Nested Loops)
# Take an integer N and print the following pattern.

num = input("Enter a number: ")
num = int(num)
for n in range(1, num + 1):
    for m in range(1, n + 1):
        print(m , end="")
    print()