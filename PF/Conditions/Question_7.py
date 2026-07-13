# Electricity Bill Calculator
# Calculate electricity bill according to:
# Units	        Rate
# First 100	    5/unit
# Next 100	    8/unit
# Above 200	    10/unit

units = int(input("Enter consumed Units:   "))
price = 0
if units < 100:
    price = units * 5
if units > 100 and units < 201:
    price = 500 + ((units - 100) * 8)
if units > 200:
    price = 500 + 800 + ((units - 200) * 10)

print(price)