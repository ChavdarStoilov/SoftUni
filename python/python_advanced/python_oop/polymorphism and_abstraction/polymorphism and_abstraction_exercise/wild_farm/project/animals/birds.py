from project.animals.animal import Bird


class Owl(Bird):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @property
    def foot_that_eat(self):
        return ['Meat']

    @property
    def eaten(self):
        return 0.25

    def make_sound(self):
        return 'Hoot Hoot'


class Hen(Bird):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @property
    def foot_that_eat(self):
        return ['Seed', 'Vegetable', 'Meat', 'Fruit']

    @property
    def eaten(self):
        return 0.35

    def make_sound(self):
        return 'Cluck'
