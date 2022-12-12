from project.person import Person

class Child(Person):

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        super().__init__(name, age)


