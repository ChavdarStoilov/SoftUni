from project.animals.animal import Mammal

class Mouse(Mammal):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def foot_that_eat(self):
        return ['Fruit', 'Vegetable']

    @property
    def eaten(self):
        return 0.1

    def make_sound(self):
        return 'Squeak'


class Dog(Mammal):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def foot_that_eat(self):
        return ['Meat']

    @property
    def eaten(self):
        return 0.4

    def make_sound(self):
        return 'Woof!'


class Cat(Mammal):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def foot_that_eat(self):
        return ['Vegetable ', 'Meat']

    @property
    def eaten(self):
        return 0.3

    def make_sound(self):
        return 'Meow'


class Tiger(Mammal):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def foot_that_eat(self):
        return ['Meat']

    @property
    def eaten(self):
        return 1.00

    def make_sound(self):
        return 'ROAR!!!'

