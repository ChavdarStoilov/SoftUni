import unittest
from project.plantation import Plantation


class TestPlantation(unittest.TestCase):

    def test__init(self):
        plantation = Plantation(20)

        self.assertEqual(20, plantation.size)
        self.assertEqual({}, plantation.plants)
        self.assertEqual([], plantation.workers)

        with self.assertRaises(ValueError) as ex:
            Plantation(-5)

        self.assertEqual('Size must be positive number!', str(ex.exception))

    def test__hiring_worker(self):
        plant = Plantation(10)
        worker = plant.hire_worker('Jonny')

        self.assertEqual('Jonny successfully hired.', worker)
        self.assertEqual(['Jonny'], plant.workers)

        with self.assertRaises(ValueError) as ex:
            plant.hire_worker('Jonny')

        self.assertEqual('Worker already hired!', str(ex.exception))

    def test__len_function(self):
        plantation = Plantation(2)

        self.assertEqual(0, len(plantation))

        plantation.hire_worker('Jonny')
        plantation.planting('Jonny', 'Rose')
        actual = len(plantation)

        self.assertEqual(1, actual)

    def test__planting(self):
        plantation = Plantation(2)

        with self.assertRaises(ValueError) as ex:
            plantation.planting('Jonny', 'Rose')

        self.assertEqual('Worker with name Jonny is not hired!', str(ex.exception))

        plantation.hire_worker('Jonny')
        first_plant = plantation.planting('Jonny', 'Rose')
        self.assertEqual('Jonny planted it\'s first Rose.', first_plant)
        self.assertEqual(['Jonny'], plantation.workers)
        self.assertEqual({'Jonny': ['Rose']}, plantation.plants)

        second_plant = plantation.planting('Jonny', 'Tree')
        self.assertEqual('Jonny planted Tree.', second_plant)
        self.assertEqual({'Jonny': ['Rose', 'Tree']}, plantation.plants)
        self.assertEqual(['Jonny'], plantation.workers)

        with self.assertRaises(ValueError) as ex_two:
            plantation.planting('Jonny', 'Shrubs')

        self.assertEqual('The plantation is full!', str(ex_two.exception))


    def test__str_function(self):
        plantation = Plantation(2)
        plantation.hire_worker('Jonny')
        plantation.planting('Jonny', 'Rose')
        plantation.hire_worker('Jon')
        plantation.planting('Jon', 'Tree')

        expect = 'Plantation size: 2\n' \
                 'Jonny, Jon\n' \
                 'Jonny planted: Rose\n' \
                 'Jon planted: Tree'

        self.assertEqual(expect, str(plantation))

    def test__repr_function(self):
        plantation = Plantation(3)
        plantation.hire_worker('Jonny')
        plantation.planting('Jonny', 'Rose')
        plantation.hire_worker('Jon')
        plantation.planting('Jon', 'Tree')

        expect = 'Size: 3\n' \
                 'Workers: Jonny, Jon'

        self.assertEqual(expect, plantation.__repr__())

if __name__ == '__main__':
    unittest.main()