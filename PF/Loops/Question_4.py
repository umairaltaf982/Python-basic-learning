# Count Digits (While Loop)
# Take an integer from the user and count how many digits it contains.

number = int(input("Enter a value:   "))
count = 0
while number > 0:
        number = number // 10
        count += 1
print(count)