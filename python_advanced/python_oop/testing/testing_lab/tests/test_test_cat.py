from testing.testing_lab.scripts.test_worker import Worker

import unittest


class WorkerTests(unittest.TestCase):
    NAME = 'Jonny'
    SALARY = 1000
    ENERGY = 2

    def test_current_init_information(self):
        the_worker = Worker(self.NAME, self.SALARY, self.ENERGY)
        actually_name = the_worker.name
        actually_salary = the_worker.salary
        actually_energy = the_worker.energy
        actually_money = the_worker.money

        self.assertEqual(self.NAME, actually_name)
        self.assertEqual(self.SALARY, actually_salary)
        self.assertEqual(self.ENERGY, actually_energy)
        self.assertEqual(0, actually_money)

    def test__energy_incremented_afet_rest__expect_increase_with_one(self):
        the_worker = Worker(self.NAME, self.SALARY, self.ENERGY)
        the_worker.rest()
        actually = the_worker.energy

        expect_result = self.ENERGY + 1

        self.assertEqual(expect_result, actually)

    def test_working_function_with_zero__expect_raise(self):
        the_worker = Worker(self.NAME, self.SALARY, 0)

        with self.assertRaises(Exception) as ex:
            the_worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_working_function_with_negative__expect_raise(self):
        the_worker = Worker(self.NAME, self.SALARY, -1)

        with self.assertRaises(Exception) as ex:
            the_worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test__decrease_energy_after_working(self):
        the_worker = Worker(self.NAME, self.SALARY, self.ENERGY)
        the_worker.work()

        actually = the_worker.energy
        expect = self.ENERGY - 1

        self.assertEqual(expect, actually)

    def test_increasing_money_after_working__expect_increase_with_the_salary(self):
        the_worker = Worker(self.NAME, self.SALARY, self.ENERGY)
        self.assertEqual(0, the_worker.money)

        the_worker.work()

        self.assertEqual(self.SALARY, the_worker.money)

        the_worker.work()

        self.assertEqual(self.SALARY * 2, the_worker.money)

    def test_checking_correct_info(self):
        the_worker = Worker(self.NAME, self.SALARY, self.ENERGY)
        actually = the_worker.get_info()
        expect = f'{self.NAME} has saved 0 money.'

        self.assertEqual(expect, actually)


if __name__ == '__main__':
    unittest.main()
