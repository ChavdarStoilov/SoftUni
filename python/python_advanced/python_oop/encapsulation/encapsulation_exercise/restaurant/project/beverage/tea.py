from project.beverage.hot_beverage import HotBeverage



class Tea(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name: str, price: float, milliliters: float):
        super().__init__(name, price, milliliters)
        