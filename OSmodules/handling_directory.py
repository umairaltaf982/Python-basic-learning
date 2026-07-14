# Handling Current Working Directory
"""
import os
cwd = os.getcwd()
print(cwd)
"""


# Changing Current Working Directory
"""
import os
def currentpath(label):
     print(f"Current working directory {label}")
     print(os.getcwd())
     print()

currentpath("Before")
os.chdir('../')
currentpath("After")
"""

# Creating and deleting a directory
"""
import os
def createDirectory(parent_path, dir_name):
    path = os.path.join(parent_path, dir_name)
    # same code for deleting the file only we use os.remove(path)
    os.mkdir(path)
    print(f"Directory Created Successfully!!!")

parent_path1 = input("Enter the Parent Path:   ")
dir_name1 = input("Enter the Directory Name:   ")
createDirectory(parent_path1, dir_name1)
"""


