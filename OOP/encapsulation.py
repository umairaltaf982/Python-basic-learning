class Employee:
    def __init__(self):
        self.name = "Umair"
        self._salary = 23
        self.__password = '35201'

    def get_cnic(self):
        return self.__password

class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.department = 'English'

    def printattr(self):

        print(f"My name is ${Employee.name}. and My salary is  ")


