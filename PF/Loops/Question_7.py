# Prime Number Checker (For Loop)
# Take an integer and determine whether it is a Prime Number or Not Prime.

num = int(num_input := input("Enter Number:   "))

if num <= 1:
    print("The number is not prime")
else:
    for n in range(2, num):
        if num % n == 0:
            print("The number is not prime")
            break
    else:
        print("The number is prime")