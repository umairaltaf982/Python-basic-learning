# Reading from a file
"""
file = open("geek.txt", "r")
content = file.read()
print(content)
file.close()
"""

# Writing in a file
# We can also use with statement because it ensure the file is closed in the end of block
"""""
with open("geek.txt", 'w') as file:            
    file.write("Now I am writing from in a file\n")
    file.write("How amazing")
"""

# Reading file line-by-line
# The code is adding each line in the file to the list
with open("geek.txt", "r") as file:
    arr = []
    for line in file:
        arr.append(line.strip())
print(arr)