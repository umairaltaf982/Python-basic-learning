import csv
import io

# Create a CSV sample in memory
csv_data = """Year,Industry,Value
2014,Manufacturing,769400
2014,Manufacturing,48000
2014,Manufacturing,12
"""
csvfile = io.StringIO(csv_data)
csvreader = csv.reader(csvfile)
for row in csvreader:
    print(row)

# Explanation: Instead of a physical file, we used StringIO to create a file-like object.
# The CSV reader parses each line into a list of values.