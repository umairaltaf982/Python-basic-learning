# Question 7 – Decorator with *args and **kwargs
# Create a decorator named logger.
# It should print:
# Function Executing...
# The decorator should support both positional and keyword arguments.
# Decorate this function:
# employee(name, salary, department="IT")


def decorator(fx):
    def mfx(*args, **kwargs):
        print("Function Executing...")
        result = fx(*args, **kwargs)
        return result
    return mfx

@decorator
def employee(name, salary, department='IT'):
    print("Employee Name:", name)
    print("Employee Salary:", salary)
    print("Employee Department:", department)

employee("Isaac", 2500)