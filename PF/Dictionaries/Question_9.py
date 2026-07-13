# Employee Management
# Create a nested dictionary for 3 employees.
# Each employee should have:
# Name
# Department
# Salary
# Tasks:
# Print all employee details.
# Increase every employee's salary by 5000.
# Print the updated dictionary.


# emp = {}
# n = 0
# while n < 3:
#     name = input("Enter your name: ")
#     emp[name] = {}
#     m = 0
#     while m < 2:
#         dept = input("Enter your department: ")
#         emp[name]["department"] = dept
#         salary = input("Enter your salary: ")
#         emp[name]["salary"] = salary
#         m += 1
#     n += 1


emp = {}
n = 0
while n < 3:
    name = input("Enter your name: ")
    emp[name] = {}
    dept = input("Enter your department: ")
    emp[name]["department"] = dept
    salary = input("Enter your salary: ")
    emp[name]["salary"] = salary
    n += 1

print(emp)