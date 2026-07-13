import datetime

x = datetime.datetime.now()
print(x)

y = datetime.datetime(2003, 9, 9)
print(y)

print(y.strftime("%B"))

print(y.strftime("%A"))

print(x.strftime("%H"))


