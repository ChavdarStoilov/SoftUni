from testing.testing_lab.scripts.car_manager import Car

import unittest


class TestCarManager(unittest.TestCase):
    MAKE = 'AUDI'
    MODEL = 'A4'
    FUEL_CONSUMPTION = 8
    FUEL_CAPACITY = 20

    def test__init_provided_information(self):
        car = Car(self.MAKE, self.MODEL, self.FUEL_CONSUMPTION, self.FUEL_CAPACITY)
        actual_make = car.make
        actual_model = car.model
        actual_consumption = car.fuel_consumption
        actual_capacity = car.fuel_capacity
        actual_fuel_amount = car.fuel_amount

        self.assertEqual(self.MAKE, actual_make)
        self.assertEqual(self.MODEL, actual_model)
        self.assertEqual(self.FUEL_CONSUMPTION, actual_consumption)
        self.assertEqual(self.FUEL_CAPACITY, actual_capacity)
        self.assertEqual(0, actual_fuel_amount)

    def test__make_checker__expect_raise_error(self):
        with self.assertRaises(Exception) as ex:
            car = Car("", self.MODEL, self.FUEL_CONSUMPTION, self.FUEL_CAPACITY)

        self.assertIsNotNone(ex)

    def test__model_checker___expect_raise_error(self):
        with self.assertRaises(Exception) as ex:
            car = Car(self.MAKE, "", self.FUEL_CONSUMPTION, self.FUEL_CAPACITY)

        self.assertIsNotNone(ex)

    def test__fuel_consumption_checker__expect_raise_error(self):
        with self.assertRaises(Exception) as ex:
            car = Car(self.MAKE, self.MODEL, -1, self.FUEL_CAPACITY)

        self.assertIsNotNone(ex)

    def test__fuel_capacity_checker__expect_raise_error(self):
        with self.assertRaises(Exception) as ex:
            car = Car(self.MAKE, self.MODEL, self.FUEL_CONSUMPTION, -1)

        self.assertIsNotNone(ex)

    def test__fuel_amount_checker__expect_raise_error(self):
        car = Car(self.MAKE, self.MODEL, self.FUEL_CONSUMPTION, self.FUEL_CAPACITY)

        with self.assertRaises(Exception) as ex:
            car.fuel_amount = -1

        self.assertIsNotNone(ex)

    def test__refuel_function__expect_add_amount_into_fuel_amount_or_raise_error(self):
        car = Car(self.MAKE, self.MODEL, self.FUEL_CONSUMPTION, self.FUEL_CAPACITY)

        car.refuel(10)
        actually = car.fuel_amount

        with self.assertRaises(Exception) as ex:
            car.refuel(0)

        self.assertIsNotNone(ex)
        self.assertEqual(10, actually)

    def test__refuel_function_for_more_than_fuel_capacity__except_fuel_amount_to_be_equal_like_capacity(self):
        car = Car(self.MAKE, self.MODEL, self.FUEL_CONSUMPTION, self.FUEL_CAPACITY)

        car.refuel(21)
        actually = car.fuel_amount
        expect = car.fuel_capacity

        self.assertEqual(expect, actually)

    def test__drive_function__expect_correct_reduced_fuel_amount_with_fuel_needed_for_provided_distance_or_raise_error(self):
        car = Car(self.MAKE, self.MODEL, self.FUEL_CONSUMPTION, self.FUEL_CAPACITY)
        car.refuel(20)
        car.drive(200)
        actually = car.fuel_amount

        with self.assertRaises(Exception) as ex:
            car.drive(300)

        self.assertIsNotNone(ex)
        self.assertEqual(4, actually)


if __name__ == '__main__':
    unittest.main()