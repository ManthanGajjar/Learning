class Person:
    def __init__(self, name):
        self.name = name

    def Talk(self):
        print(f"{self.name} Talk")

person = Person("John Doe")
person.Talk()
# prints name
# print(person.name)