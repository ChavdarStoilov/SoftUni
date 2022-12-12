from abc import ABC, abstractmethod


class Food(ABC):

    def __init__(self, quantity: int):
        self.quantity = quantity

    @abstractmethod
    def feed_food(self, food):
        pass

class Vegetable(Food):

    def __init__(self, quantity: int):
        super().__init__(quantity)

    def feed_food(self, food):
        pass



class Fruit(Food):

    def __init__(self, quantity: int):
        super().__init__(quantity)

    def feed_food(self, food):
        pass


class Meat(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)

    def feed_food(self, food):
        pass


class Seed(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)

    def feed_food(self, food):
        pass
