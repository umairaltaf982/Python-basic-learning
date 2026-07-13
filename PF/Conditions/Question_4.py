# Grade Calculator
# Take marks (0–100) and assign grades:
# Marks	    Grade
# 90-100	A
# 80-89	    B
# 70-79	    C
#60-69	    D
# Below 60	Fail

marks = int(input("Enter marks: "))
if marks in range(90, 101):
    print("A")
elif marks in range(80, 90):
    print("B")
elif marks in range(70, 80):
    print("C")
elif marks in range(60, 70):
    print("D")
elif marks in range(0, 60):
    print("Fail")
else:
    print("inappropriate Marks")
