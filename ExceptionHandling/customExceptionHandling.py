# User-defined exceptions are created by defining a new class that inherits from
# Python's built-in Exception class or one of its subclasses.
# Steps:
#     Step 1: Define a New Exception Class: Create a new class that inherits from Exception or any of its subclasses.
#     Step 2: Raise the Exception: Use the raise statement to raise the user-defined exception when a specific condition occurs.
#     Step 3: Handle the Exception: Use try-except blocks to handle the user-defined exception.

# Step 1:
class InvalidAgeError(Exception):
    def __init__(self, age, msg = 'Age must be between 18 to 120'):
        self.age = age
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.age} -> {self.msg}'

# Step 2:
def set_age(age):
    if age <= 18 or age >= 120:
        raise InvalidAgeError(age)
    else:
        print(f"Age set to: {age}")

# Step 3:
try:
    set_age(17)
except InvalidAgeError as e:
    print(e)