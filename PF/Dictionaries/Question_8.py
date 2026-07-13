# Nested Dictionary
# Create a nested dictionary for three students.
# Example:
# students = {
#     "student1": {
#         "name": "Ali",
#         "age": 20
#     },
#     "student2": {
#         "name": "Ahmed",
#         "age": 22
#     },
#     "student3": {
#         "name": "Sara",
#         "age": 21
#     }
# }
# Print the name and age of each student using loops.


students = {
    "student1": {
        "name": "Ali",
        "age": 20
    },
    "student2": {
        "name": "Ahmed",
        "age": 22
    },
    "student3": {
        "name": "Sara",
        "age": 21
    }
}

for key, value in students.items():
    for key1, value1 in value.items():
        print(f"{key} -> {key1} -> {value1}")