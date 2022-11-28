from project.meals.meal import Meal


class Dessert(Meal):
    QUANTITY = 30

    def __init__(self, name, price, quantity = None):
        super().__init__(name, price, self.QUANTITY)


    def details(self):
        return f'Dessert {self.name}: {self.price:.2f}lv/piece'