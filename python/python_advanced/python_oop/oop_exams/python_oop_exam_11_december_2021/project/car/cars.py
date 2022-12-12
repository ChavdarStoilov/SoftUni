from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar

class Cars:

    CARS = {
        'MuscleCar': MuscleCar,
        'SportsCar': SportsCar
    }

    def __init__(self, type_car, model, speed_limit):
        self.type_car = type_car
        self.model = model
        self.speed_limit = speed_limit

    def create_cars(self):
        return self.CARS[self.type_car](self.model, self.speed_limit)