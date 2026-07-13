# Create a dictionary containing the marks of 5 subjects.
# Example:
# marks = {
#     "Math": 88,
#     "English": 75,
#     "Physics": 91,
#     "Chemistry": 84,
#     "Computer": 95
# }
# Tasks:
# Print each subject with its marks.
# Update the English marks to 82.
# Delete the Chemistry entry.
# Print the final dictionary.


marks = {
    "Math": 88,
    "English": 75,
    "Physics": 91,
    "Chemistry": 84,
    "Computer": 95
}

for key, value in marks.items():
    print(f"{key}: {value}")

marks["English"] = 82

marks.pop("Chemistry")

print(marks)