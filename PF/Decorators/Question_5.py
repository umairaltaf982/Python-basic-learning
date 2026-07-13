# Question 5 – Decorator Using **kwargs
# Create a decorator show_kwargs.
# Before executing the function, print all keyword arguments.
# Decorate a function:
# student(name, age, city)
# Call the function using keyword arguments.


def show_kwargs(fx):
    def mfx(**kwargs):
        print(kwargs)
        return fx(**kwargs)
    return mfx

@show_kwargs
def student(name, age, city):
    print(f"The student name is {name} and age is {age}, city is {city}")

student(name = "Umair", age = 21, city = "Lahore")