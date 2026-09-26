class EmptyListError(Exception):
    pass



def top_students(stud):
    if len(stud) == 0:
        raise EmptyListError("Student list is empty")
    for key in stud:
        print(f'({key})')

students = [
    {"name": "Ali", "grade": 78},
    {"name": "Sara", "grade": 91},
    {"name": "Zain", "grade": 85},
]

top_students(students)
