
# Single Inheritance: Single inheritance enables a derived class to inherit properties from a single parent class,
#   thus enabling code reusability and the addition of new features to existing code.
"""
# Base Class
class Parent:
    def func1(self):
        print("This function is in parent class.")

# Derived Class
class Child(Parent):
    def func2(self):
        print("This function is in child class.")

obj = Child()
obj.func1()
obj.func2()
"""

# Multiple Inheritance: When a class can be derived from more than one base class this type of inheritance is called multiple inheritances.
# 	In multiple inheritances, all the features of the base classes are inherited into the derived class.
"""
# Base class 1
class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)

# Base class 2
class Father:
    fathername = ""
    def father(self):
        print(self.fathername)

# Derived class
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)

# Driver code
s1 = Son()
s1.fathername = "John"
s1.mothername = "Marry"
s1.parents()
"""

# Multilevel Inheritance: In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class.
# 	This is similar to a relationship representing a child and a grandfather.
"""
# Base class
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

# Intermediate class
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        # Call the constructor of Grandfather
        Grandfather.__init__(self, grandfathername)

# Derived class
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        # Call the constructor of Father
        Father.__init__(self, fathername, grandfathername)

    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print('Father name :', self.fathername)
        print('Son name :', self.sonname)

# Driver code
s1 = Son('Umair', 'Altaf', 'Ilm Deen')
print(s1.grandfathername)
s1.print_name()
"""

# Hierarical Inheritance: When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance.
"""
# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")

# Derived class 1
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")

# Derived class 2
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")

# Driver code
object1 = Child1()
object2 = Child2()

object1.func1()
object1.func2()
object2.func1()
object2.func3()
"""

# Hybrid Inheritance: Hybrid inheritance is a combination of more than one type of inheritance.
# 	It uses a mix like single, multiple, or multilevel inheritance within the same program.
"""
# Base class
class School:
    def func1(self):
        print("This function is in school.")

# Derived class 1 (Single Inheritance)
class Student1(School):
    def func2(self):
        print("This function is in student 1.")

# Derived class 2 (Another Single Inheritance)
class Student2(School):
    def func3(self):
        print("This function is in student 2.")

# Derived class 3 (Multiple Inheritance)
class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")

# Driver code
obj = Student3()
obj.func1()
obj.func2()
"""