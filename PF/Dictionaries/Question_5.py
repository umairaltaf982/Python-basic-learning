# 5. Loop Through a Dictionary
# Given:
# person = {
#     "name": "Sara",
#     "age": 22,
#     "city": "Karachi"
# }
# Using loops, print:
# name : Sara
# age : 22
# city : Karachi

person = {
    "name": "Sara",
    "age": 22,
    "city": "Karachi"
}

for key, value in person.items():
    print(key,": ", value)