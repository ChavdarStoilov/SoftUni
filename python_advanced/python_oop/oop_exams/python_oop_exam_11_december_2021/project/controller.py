from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        cars = {
            'MuscleCar': MuscleCar,
            'SportsCar': SportsCar
        }
        for car in self.cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")

        if car_type in ['MuscleCar', 'SportsCar']:
            self.cars.append(cars[car_type](model, speed_limit))
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):

        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")

        self.drivers.append(Driver(driver_name))
        return f'Driver {driver_name} is created.'

    def create_race(self, race_name: str):

        for race in self.races:
            if race.name == race_name:
                raise Exception(f'Race {race_name} is already created!')

        self.races.append(Race(race_name))
        return f'Race {race_name} is created.'

    def get_car_instance(self, car_type):

        for idx in range(len(self.cars) -1, -1, -1):
            car = self.cars[idx]
            if car.__class__.__name__ == car_type:
                if not car.is_taken:
                    return car

        return False

    def add_car_to_driver(self, driver_name: str, car_type: str):

        for driver in self.drivers:
            if driver.name == driver_name:
                car = self.get_car_instance(car_type)

                if not car:
                    raise Exception(f'Car {car_type} could not be found!')
                
                if driver.car:
                    old_car_model = driver.car
                    old_car_model.is_taken = False
                    driver.car = car
                    car.is_taken = True
                    return f'Driver {driver_name} changed his car from {old_car_model.model} to {car.model}.'

                driver.car = car
                car.is_taken = True
                return f'Driver {driver_name} chose the car {car.model}.'

        raise Exception(f'Driver {driver_name} could not be found!')


    def get_driver_instance(self, driver):
        for drivers in self.drivers:
            if driver == drivers.name:
                return drivers

        return False

    def add_driver_to_race(self, race_name: str, driver_name: str):
        driver = self.get_driver_instance(driver_name)

        if not driver:
            raise Exception(f'Driver {driver_name} could not be found!')

        for race in self.races:
            if race.name == race_name:
                if driver in race.drivers:
                    raise Exception(f'Driver {driver_name} is already added in {race_name} race.')

                if not driver.car:
                    raise Exception(f'Driver {driver_name} could not participate in the race!')

                race.drivers.append(driver)
                return f'Driver {driver_name} added in {race_name} race.'

        raise Exception(f'Race {race_name} could not be found!')

    def start_race(self, race_name: str):

        for race in self.races:
            if race.name == race_name:
                if len(race.drivers) < 3:
                    raise Exception(f'Race {race_name} cannot start with less than 3 participants!')


                drivers = {driver: driver.car.speed_limit for driver in race.drivers}

                sorted_drivers = sorted(drivers.items(), key=lambda x: x[1], reverse=True)

                result = ''
                winners = 3
                for driver, speed_limit in sorted_drivers:
                    if winners == 0:
                        break

                    driver.number_of_wins += 1
                    result += f'Driver {driver.name} wins the {race_name} race with a speed of {speed_limit}.\n'
                    winners -= 1

                return result.strip()

        raise Exception(f'Race {race_name} could not be found!')