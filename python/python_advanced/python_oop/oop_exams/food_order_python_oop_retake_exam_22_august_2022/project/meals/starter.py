from project.meals.meal import Meal


class Starter(Meal):
    QUANTITY = 60

    def __init__(self, name, price, quantity=None):
        super().__init__(name, price, self.QUANTITY)

    def details(self):
        return f'Starter {self.name}: {self.price:.2f}lv/piece'
