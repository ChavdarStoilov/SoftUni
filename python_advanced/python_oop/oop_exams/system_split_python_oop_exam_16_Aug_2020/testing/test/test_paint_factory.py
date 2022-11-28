from project.factory.paint_factory import PaintFactory

import unittest


class TestFactory(unittest.TestCase):
    NAME = 'Jonny'
    CAPACITY = 100

    def test__init(self):
        paint_factory = PaintFactory(self.NAME, self.CAPACITY)

        actual_name = paint_factory.name
        actual_capacity = paint_factory.capacity
        actual_ingredients = paint_factory.ingredients
        actual_valid_ingredients = paint_factory.valid_ingredients

        self.assertEqual(self.NAME, actual_name)
        self.assertEqual(self.CAPACITY, actual_capacity)
        self.assertEqual({}, actual_ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], actual_valid_ingredients)

    def test__adding_ingredient(self):
        paint_factory = PaintFactory(self.NAME, self.CAPACITY)

        paint_factory.add_ingredient('blue', 20)

        actual_added = paint_factory.ingredients['blue']

        self.assertEqual(20, actual_added)

        with self.assertRaises(ValueError) as ex:
            paint_factory.add_ingredient('blue', 2000)

        self.assertEqual('Not enough space in factory', str(ex.exception))

        with self.assertRaises(TypeError) as ex_two:
            paint_factory.add_ingredient('Black', 10)

        self.assertEqual('Ingredient of type Black not allowed in PaintFactory', str(ex_two.exception))


    def test__remove_ingredient(self):
        paint_factory = PaintFactory(self.NAME, self.CAPACITY)

        paint_factory.add_ingredient('blue', 30)
        paint_factory.remove_ingredient('blue', 10)

        actual_quantity = paint_factory.ingredients['blue']

        self.assertEqual(20, actual_quantity)

        with self.assertRaises(ValueError) as ex:
            paint_factory.remove_ingredient('blue', 100)

        self.assertEqual('Ingredients quantity cannot be less than zero', str(ex.exception))

        with self.assertRaises(KeyError) as ex_two:
            paint_factory.remove_ingredient('yellow', 10)

        self.assertEqual("'No such ingredient in the factory'", str(ex_two.exception))


    def test__get_products(self):
        paint_factory = PaintFactory(self.NAME, self.CAPACITY)
        paint_factory.add_ingredient('blue', 30)
        paint_factory.add_ingredient('yellow', 30)
        paint_factory.add_ingredient('red', 20)

        actual = paint_factory.products
        expect = {
            'blue': 30,
            'yellow': 30,
            'red': 20
        }

        self.assertEqual(expect, actual)

if __name__ == '__main__':
    unittest.main()