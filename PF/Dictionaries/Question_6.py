# Print Only Keys and Then Only Values
# Given:
# fruit = {
#     "apple": 150,
#     "banana": 80,
#     "orange": 200
# }
# Print:
# Only the keys.
# Only the values.
# Use loops for both.


fruit = {
    "apple": 150,
    "banana": 80,
    "orange": 200
}

for key in fruit.keys():
    print(f"{key}")

for value in fruit.values():
    print(f"{value}")