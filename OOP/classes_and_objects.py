class Person:
    name = "umair"
    age = 23
    occupation = "Software Engineer"

    def info(self):
        print(f"{self.name} is a {self.occupation} and he is {self.age} years old.")

a = Person()
a.info()
a.name = "Ammar"
a.age = 21
a.occupation = "Web Developer"
a.info()