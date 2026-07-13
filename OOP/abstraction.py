from abc import ABC, abstractmethod


#Abstract Method
"""
class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass #abstract method

class English(Greet):
    def say_hello(self):
        return "Hello Everyone"

eng = English()
print(eng.say_hello())
"""


#Abstract Properties
class Animal(ABC):
    @property
    @abstractmethod
    def species(self):
        pass    #Abstract property, Must be implemented by subclass, without it the code will not execute

class Dog(Animal):
    @property
    def species(self):
        return "German Shepherd"

    def say_hello(self):
        return "Hello!!!"

d = Dog()
print(d.species)