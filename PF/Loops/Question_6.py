# Factorial of a Number (For Loop)
# Take an integer N and calculate its factorial.

num = int(input("Enter a number: "))
ans = 1
if num > 0:
    for n in range(1, num+1):
        ans = ans * n
    print(f"{ans}")
elif num == 0:
    print("1")
else:
    print("Number is Negative")
