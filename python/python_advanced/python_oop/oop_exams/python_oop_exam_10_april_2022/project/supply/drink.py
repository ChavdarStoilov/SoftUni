from project.supply.supply import Supply


class Drink(Supply):
    DEFAULT_ENERGY = 15

    def __init__(self, name):
        super().__init__(name, self.DEFAULT_ENERGY)
