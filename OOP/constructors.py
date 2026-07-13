class person:

    def __new__(cls, *args, **kwargs):
        print("I always called before __init__ and used to create the instance")
        return super(person,cls ).__new__(cls)

    def __init__(self, n, o):
        print("Hello Everyone!!!")
        self.name = n
        self.occupation = o

    def __str__(self):
        return "Whenever you \"print\" an object, I will appear!!!"

    def info(self):
        print(f"Name of person is {self.name} and occupation is {self.occupation}")

a = person("John", "Software Engineer")
print(a)
a.info()
b = person("Bob", "Software Engineer")
b.info()