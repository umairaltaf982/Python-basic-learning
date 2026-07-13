import json
with open("sample1.json", "r") as jsonfile:
    data = json.load(jsonfile)
    print(data)

# Explanation: The JSON file content is converted into a Python dictionary, which can be used directly in programs.