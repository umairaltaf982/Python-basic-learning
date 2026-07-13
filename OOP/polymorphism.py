# Compile-time Polymorphism (Method/Function Overloading)
# Compile-time polymorphism involves selecting a method or operation before program execution,
# typically through method or operator overloading.

# Python does not support true compile-time polymorphism because method calls are resolved at runtime.
# However, similar behavior can be achieved using default arguments, variable-length arguments (*args), or keyword arguments (**kwargs).
"""
class Calculator:
    def multiply(self, a = 1, b = 2 , *args):
        result = a * b
        for num in args:
            result *= num
        print(result)

calc = Calculator()
calc.multiply()
calc.multiply(5)
calc.multiply(1, 2)
calc.multiply(2, 3, 4, 5)
"""



# Runtime Polymorphism (Method/Function Overriding)
# Runtime polymorphism means that the behavior of a method is decided while program is running, based on the object calling it.
# This happens through Method Overriding a child class provides its own version of a method already defined in the parent class.
"""
class Animal:
    def sound(self):
        print("Not any specific Animal")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

animals = [Cat(), Dog(), Animal()]
for animal in animals:
    animal.sound()
"""