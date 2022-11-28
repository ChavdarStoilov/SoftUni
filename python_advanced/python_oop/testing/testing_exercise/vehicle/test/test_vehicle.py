from project.vehicle import Vehicle

import unittest


class TestVehicle(unittest.TestCase):
    FUEL = 60
    HORSE_POWER = 250

    def test__all_attributes__init_and_class(self):
        vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

        self.assertEqual(self.FUEL, vehicle.fuel)
        self.assertEqual(self.FUEL, vehicle.capacity)
        self.assertEqual(self.HORSE_POWER, vehicle.horse_power)
        self.assertEqual(vehicle.DEFAULT_FUEL_CONSUMPTION, vehicle.fuel_consumption)

    def test__driving_function__first_expect_correct_result__second_raise_error(self):
        vehicle = Vehicle(self.FUEL, self.HORSE_POWER)
        vehicle.drive(25)

        actual = vehicle.fuel
        expect = self.FUEL - 31.25

        self.assertEqual(expect, actual)

        with self.assertRaises(Exception) as ex:
            vehicle.drive(200)

        self.assertEqual('Not enough fuel', str(ex.exception))

    def test__refuel_function__first_expect_correct_result__second_raise_error(self):
        vehicle = Vehicle(self.FUEL, self.HORSE_POWER)
        vehicle.drive(10)
        vehicle.refuel(10)

        actual = vehicle.fuel
        expect = 57.5

        self.assertEqual(expect, actual)

        vehicle.drive(20)
        with self.assertRaises(Exception) as ex:
            vehicle.refuel(50)

        self.assertEqual('Too much fuel', str(ex.exception))


    def test__str_result(self):
        vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

        actual = str(vehicle)
        expect = f"The vehicle has {self.HORSE_POWER} " \
                 f"horse power with {self.FUEL} fuel left and {vehicle.DEFAULT_FUEL_CONSUMPTION} fuel consumption"


        self.assertEqual(expect, actual)