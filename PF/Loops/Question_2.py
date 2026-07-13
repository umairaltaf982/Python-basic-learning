# Sum of First N Natural Numbers (For Loop)
# Take a number N and calculate the sum of the first N natural numbers using a for loop.

num = int(input("Enter a value:   "))
sum = 0
for x in range(1 , num + 1):
    sum += x
print(f"The sum of numbers till that value is: {sum}")