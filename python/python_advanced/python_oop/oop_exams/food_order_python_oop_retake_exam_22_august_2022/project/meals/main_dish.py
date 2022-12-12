from project.meals.meal import Meal


class MainDish(Meal):
    QUANTITY = 50

    def __init__(self, name, price, quantity = None):
        super().__init__(name, price, self.QUANTITY)


    def details(self):
        return f'Main Dish {self.name}: {self.price:.2f}lv/piece'