class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_person(self):
        print(f"Name: {self.name}\nAge: {self.age}")