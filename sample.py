class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHi(self):
        print(self.name)

    def print_all(self):
        getattr(self)



john = User('John', 25)
john.print_all()