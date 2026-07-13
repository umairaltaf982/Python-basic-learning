from dataclasses import replace

print("hello World")

name = "Ali"
age = 23
height = 72.3
print(name, age, height)

i , f = 21, 22
print(i)
print(f)
print(i, f)
 
"""
g = int(input("Enter your height: "))
print(g)
"""

print("My weight is: ", 70, ". My height is: ", 172.5)

""""
Hello my name is Umair Altaf
I am from Lahore Pakistan
Have a good day
"""


x = "John"

def myfunc1():
	x = "Ali"
	print("My name is " + x)    
myfunc1()

print("My name is: " + x)


b = "Hello, World!"
print(b[2:5])

a = "Hello World!"
print(a.replace("l", "ww"))

# F-string
age = 35
txt = f"hello, My age is {age}"
print(txt)


price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


print("Hello it's alright to be \'Bad\' ")

print(bool("Hello"))
print(bool("2"))