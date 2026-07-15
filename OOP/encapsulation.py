class Employee:
    def __init__(self):
        self.name = "Umair"          # Public
        self._salary = 23            # Protected
        self.__password = "35201"    # Private

    def get_cnic(self):
        return self.__password


class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.department = "English"

    def printattr(self):
        print(f"My name is {self.name}.")
        print(f"My salary is {self._salary}.")
        print(f"My department is {self.department}.")
        print(f"My password is {self.get_cnic()}")   # Accessing private variable through getter


# Create object
manager = Manager()

# Call method
manager.printattr()