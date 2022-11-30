import unittest
from project.plantation import Plantation


class TestPlantation(unittest.TestCase):
    def test_plantation_init(self):
        self.pl = Plantation(1)
        self.assertEqual(self.pl.size, 1)

    def test_invalid_error_message(self):
        with self.assertRaises(ValueError) as ve:
            self.pl = Plantation(-1)
        self.assertEqual(str(ve.exception), 'Size must be positive number!')

    def test_len_wrong_count(self):
        self.pl = Plantation(1)
        self.pl.hire_worker('Martin')
        self.pl.plants['Martin'] = ['Tomatoes']
        self.assertEqual(self.pl.__len__(), 1)

    def test_len_wrong_iterable(self):
        self.pl = Plantation(1)
        self.pl.hire_worker('Alexandra')
        self.pl.plants['Alexandra'] = ['plant']
        self.assertEqual(self.pl.__len__(), 1)

    def test_len_not_addition(self):
        self.pl = Plantation(1)
        self.pl.hire_worker('Martin')
        self.pl.hire_worker('Alexandra')
        self.pl.plants['Martin'] = ['Tomatoes']
        self.pl.plants['Alexandra'] = ['plant']
        self.assertEqual(self.pl.__len__(), 2)

    # def test_hire_worker_wrong_if(self):
    #     self.pl = Plantation(1)
    #     self.assertEqual(self.pl.hire_worker('Martn'), 'Martin successfully hired.')

    def test_hire_worker_wrong_error_message(self):
        self.pl = Plantation(1)
        self.pl.hire_worker('Martin')
        with self.assertRaises(ValueError) as ve:
            self.pl.hire_worker('Martin')
        self.assertEqual(str(ve.exception), 'Worker already hired!')

    def test_hire_worker_wrong_append(self):
        self.pl = Plantation(1)
        result = self.pl.hire_worker('Martin')
        self.assertEqual(len(self.pl.workers), 1)
        self.assertEqual(result, 'Martin successfully hired.')

    def test_planting_wrong_error_not_hired(self):
        self.pl = Plantation(1)
        with self.assertRaises(ValueError) as ve:
            self.pl.planting('Martin', 'carrots')
        self.assertEqual(str(ve.exception), 'Worker with name Martin is not hired!')

    def test_planting_wrong_error_message(self):
        self.pl = Plantation(1)
        self.pl.hire_worker('Martin')
        self.pl.planting('Martin', 'carrots')
        with self.assertRaises(ValueError) as ve:
            self.pl.planting('Martin', 'Tomatoes')
        self.assertEqual(str(ve.exception), 'The plantation is full!')

    def test_planting_wrong_dict_assigment(self):
        self.pl = Plantation(2)
        self.pl.hire_worker('Martin')
        self.pl.planting('Martin', 'Radishes')
        self.pl.planting('Martin', 'carrots')
        self.assertEqual(len(self.pl.plants['Martin']), 2)

    def test_planting_wrong_message(self):
        self.pl = Plantation(2)
        self.pl.hire_worker('Martin')
        self.pl.planting('Martin', 'Radishes')
        self.assertEqual(self.pl.planting('Martin', 'Radishes'), 'Martin planted Radishes.')

    def test_planting_new_planting_not_added(self):
        self.pl = Plantation(2)
        self.pl.hire_worker('Martin')
        self.pl.planting('Martin', 'Radishes')
        self.assertEqual(len(self.pl.plants['Martin']), 1)

    def test_planting_new_planting(self):
        self.pl = Plantation(2)
        self.pl.hire_worker('Martin')
        self.assertEqual(self.pl.planting('Martin', 'Radishes'), 'Martin planted it\'s first Radishes.')

    def test_str_wrong_output(self):
        self.assertEqual(Plantation(2).__str__().strip(), 'Plantation size: 2')
        self.pl = Plantation(2)
        self.pl.hire_worker('Martin')
        self.pl.planting('Martin', 'Radishes')
        self.assertEqual(self.pl.__str__().strip(), 'Plantation size: 2\nMartin\nMartin planted: Radishes')

    def test_repr_wrong_output(self):
        self.assertEqual(Plantation(2).__repr__().strip(), 'Size: 2\nWorkers:')
        self.pl = Plantation(2)
        self.pl.hire_worker('Martin')
        self.pl.planting('Martin', 'Radishes')
        self.assertEqual(self.pl.__repr__().strip(), 'Size: 2\nWorkers: Martin')


if __name__ == '__main__':
    unittest.main()