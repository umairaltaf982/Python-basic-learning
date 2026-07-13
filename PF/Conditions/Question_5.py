# Leap Year Checker
# Take a year as input and determine whether it is a leap year.
# Rules:
# Divisible by 400 → Leap Year
# Divisible by 100 → Not Leap Year
# Divisible by 4 → Leap Year
# Otherwise → Not Leap Year

year = int(input("Enter the Year: "))

if year % 4 == 0 and year % 400 == 0:
    print("Leap Year!!!")
else:
    print("Not Leap Year!!!")