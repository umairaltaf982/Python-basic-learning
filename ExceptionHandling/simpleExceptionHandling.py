# Exception Handling allows a program to handle unexpected errors during execution in a controlled way,
# instead of crashing abruptly. It enables programs to detect errors, manage them properly and
# continue execution wherever possible.

"""
n = 10
try:
    res = n / 0
except ZeroDivisionError:
    print("Can't be divided by zero!")
"""

# There are four steps to write a code with exception handling
# try: Runs the risky code that might cause an error.
# except: Catches and handles the error if one occurs.
# else: Executes only if no exception occurs in try.
# finally: Runs regardless of what happens useful for cleanup tasks like closing files.
"""
try:
    n = 0
    res = 100 / n

except ZeroDivisionError:
    print("You can't divide by zero!")

except ValueError:
    print("Enter a valid number!")

else:
    print("Result is", res)

finally:
    print("Execution complete.")
"""



