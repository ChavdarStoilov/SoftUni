from project.animal import Animal

class Lion(Animal):
    cost_money = 50

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age)
        self.money_for_care += self.cost_money