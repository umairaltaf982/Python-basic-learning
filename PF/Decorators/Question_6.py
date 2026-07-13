# Question 6 – Multiple Decorators
# Create two decorators:
# Decorator 1:
# Starting...
# Decorator 2:
# Checking permissions...
# Decorate a function delete_file() using both decorators and observe the execution order.


def start_dec(func):
    def mfx():
        print("Starting...")
        func()
    return mfx

def permission_dec(func):
    def mfx():
        func()
        print("Checking permissions...")
    return mfx

@start_dec
@permission_dec
def delete_files():
    print("Want to delete files??")

delete_files()