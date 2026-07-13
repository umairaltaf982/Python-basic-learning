# WAP to display the last digit of a number
"""
x = int(input("Enter a number: "))
if x < 10:
    print(x)

else:
    print(x % 10)
"""


# WAP to check if a single character is a vowel or not.
"""
vowel = "aeiou"
alpha = input("Enter a single Character: ")
if len(alpha) > 1:
    print("The length is not appropriate")
else:
    if alpha in vowel:
        print(f"The \"{alpha}\" is vowel")
    else:
        print(f"The \"{alpha}\" is not vowel")
"""


# Check if the first and last number of a list is same or not. Take a pre-defined list in the code itself.
"""
mylist = [1, 2, 3, 4, 1]
a = mylist[0]
b = mylist[len(mylist) - 1]
if a == b:
    print("The values are same")
else:
    print("Different Values")
"""


# WAP to convert a celsius value to fahrenheit and vice versa
"""
temp = input("Enter temperature (e.g. 32C or 96F): ")
temp_split = temp[0:(len(temp)-1)]
temp_num = int(temp_split)
if temp[-1] == "F":
    cel = temp_num * (5 / 9) - 32
    print(f"Celsius: {cel}C")
elif temp[-1] == "C":
    fah = temp_num * (9 / 5) + 32
    print(f"Celsius: {fah}C")
else:
    print("Inappropriate Temperature Type")
"""


# WAP to check whether a person is eligible to vote or not based on their age.
"""
age = int(input("Enter the age of the person:  "))
result = "Eligible" if age >= 18 else "Not-Eligible"
print(result)
"""


# WAP to check using the sides of a triangle to tell if it is equilateral triangle or not.
"""
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
if a == b == c:
    print("Given Triangle is Equilateral Triangle")
else:
    print("Given Triangle is not a Equilateral Triangle")
"""


# WAP to check if the 2nd last digit of numerical input from the user is divisible by 3 or not
"""
num = int(input("Enter a Number:   "))
if num > 9:
    temp = num % 100
    div = temp // 10
    if div % 3 == 0:
        print("The second last digit is divisible by 3")
    else:
        print("The second last digit is not divisible by 3")
"""


# WAP to print the day based on the number input.
# For example: if input = 1, output = Monday
"""
day_digit = int(input("Enter the day digit (1-7):   "))
match day_digit:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid!\nPlease Enter between 1-7")
"""