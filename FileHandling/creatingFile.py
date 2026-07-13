# creating txt file
"""
try:
    with open("file.txt", "x", encoding="utf-8") as f:
        f.write("hello world")
except FileExistsError:
    print("file.txt already exists, exclusive creation aborted.")
"""


# creating a binary file
"""
try:
    with open("file.bin", "wb") as f:
        f.write(b'\x00\x01\x02\x03\x04')
except FileExistsError:
    print("file.bin already exists, exclusive creation aborted.")

with open("file.bin", "rb") as f:
    content = f.read()
    print(content)
"""