# Print a Square Pattern
# Take an integer N and print an N × N square made of *.

num = int(input("Enter a number: "))
for n in range(num):
    for m in range(num):
        print("*", end=" ")
    print()