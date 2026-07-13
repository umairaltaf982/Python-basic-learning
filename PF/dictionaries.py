"""
# Create and print a dictionary
info = {
    "name": "Ali",
    "age": 21,
    "city": "Lahore"
}
print(info)

# Access Values
print(f"The age of {info["name"]} is: {info["age"]}")

# Get Values
print(info.get("name"))

# Get Keys
print(info.keys())

# Add a New Key
info["degree"] = "Software Engineering"
print(info)

# Update a Value
info["degree"] = "SE"
print(info)

# delete a key-value
info.pop("degree")
print(info)

# Check Key Existence
if "age" in info:
    print(info["age"])

# Character Frequency count
word = input("Enter a word:   ")
freq = {}
for char in word:
    freq[char] = freq.get(char, 0) + 1
print(freq)
"""


# Count Frequency of Elements
"""
numbers = [1, 2, 3, 1, 2, 1, 4]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print(frequency)
"""


# Store marks of 5 subjects in a dictionary and calculate
"""
marks = {
    "Maths" : 50,
    "Science" : 50,
    "English" : 49
}
sum = 0
count = 0
for m in marks.values():
    sum += m
    count += 1
print(f"The average of marks is:     {sum/count}")
"""


# Find the student with the highest marks.(Most Pythonic)
"""
marks = {
    "Ali": 85,
    "Ahmed": 92,
    "Sara": 88
}
topper = max(marks, key=marks.get)
maximum = marks[topper]
print(f"The topper is {topper}, and marks are {maximum}")
"""


# Find the student with the highest marks.(Manual Code)
"""
marks = {
    "Ali": 85,
    "Ahmed": 92,
    "Sara": 88
}
topper = None
maximum = 0
for name, score in marks.items():
    if score > maximum:
        maximum = score
        topper = name
print(f"The topper is {topper}, and marks are {maximum}")
"""


# Merge them into a single dictionary(Manual Way)
"""
dict1 = {
    "a":1,
    "b":2
}
dict2 = {
    "c":3,
    "d":4
}
dict = {}
for alpha, num in dict1.items():
    dict[alpha] = num
for alpha, num in dict2.items():
    dict[alpha] = num
print(dict)
"""


# Merge them into a single dictionary(Pythonic way)
"""
dict1 = {
    "a":1,
    "b":2
}
dict2 = {
    "c":3,
    "d":4
}
dict = dict1.update(dict2)
print(dict1)
"""


# Create a dictionary containing squares of numbers from 1 to 10.
"""
dict = {}
n = 1
while n <= 10:
    dict[n] = n**2
    n += 1
print(dict)
"""


# Take a sentence from the user and count frequency of each word.
"""
sentence = input("Enter a sentence: ")
words = sentence.split()
freq = {}
for num in words:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)
"""


# Create a user defined dictionary
"""
i = int(input("How many key-values you want to enter:   "))
dict = {}
n = 0
while n < i:
    key = input("Enter the key:   ")
    value = input(f"Enter value for {key}:   ")
    dict[key] = value
    n += 1
print(dict)
"""

# Invert a Dictionary
"""
dict = {
    "a":1,
    "b":2,
    "c":3
}
new_dict = {}
for alpha, num in dict.items():
    new_dict[num] , alpha = alpha , num
print(new_dict)
"""


# Store information of 3 students and Print details of a student by roll number
"""
i = int(input("Enter number of Students:   "))
j = int(input("How many key-value pairs you want to enter:   "))
n = 0
dict = {}
while n < i:
    roll_no = input("Enter the roll number of Student:   ")
    dict[roll_no] = {}
    m = 0
    while m < j:
        key = input("Enter the key:   ")
        value = input("Enter the value:   ")
        dict[roll_no][key] = value
        m += 1
    n += 1
print("\nFinal Dictionary:", dict)
"""


