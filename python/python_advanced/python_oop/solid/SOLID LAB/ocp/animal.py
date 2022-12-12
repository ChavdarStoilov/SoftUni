from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def get_species(self):
        pass

class Dog(Animal):
    def get_species(self):
        return 'woof-woof'


class Cat(Animal):
    def get_species(self):
        return 'meow'


class Chicken(Animal):
    def get_species(self):
        return 'clucking'


animals = [Cat, Dog, Chicken]
for animal in animals:
    print(animal.get_species())

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
