"""
Create the following tests:
•	Cat's size is increased after eating
•	Cat is fed after eating
•	Cat cannot eat if already fed, raises an error
•	Cat cannot fall asleep if not fed, raises an error
•	Cat is not sleepy after sleeping

"""
from testing.testing_lab.scripts.test_cat import Cat
import unittest
from unittest import TestCase




class CatTests(TestCase):

    def test_init_information(self):
        cat = Cat('Tommy')
        self.assertEqual('Tommy', cat.name)
        self.assertEqual(False, cat.fed)
        self.assertEqual(False, cat.sleepy)
        self.assertEqual(0, cat.size)


    def test_cat_size_after_eat__expect_to_be_increase_by_one(self):
        cat = Cat('Pop')

        cat.eat()

        self.assertEqual(1, cat.size)

    def test_cat_is_fed_and_cannot_eat_after_already_is_fed__expect_raise_error_and_true_on_fed(self):
        cat = Cat('Jonny')
        cat.eat()

        with self.assertRaises(Exception) as content:
            cat.eat()

        self.assertIsNotNone(content)
        self.assertEqual(True, cat.fed)
        self.assertEqual(True, cat.sleepy)

    def test_cat_cannot_go_to_sleep_when_is_hungry__expect_raise_error_and_fed_false(self):
        cat = Cat('Bunny')

        with self.assertRaises(Exception) as content:
            cat.sleep()

        self.assertIsNotNone(content)
        self.assertEqual(False, cat.fed)


    def test_cat_is_not_sleepy_after_already_sleeping__expect_sleepy_to_be_false(self):
        cat = Cat('Sho')
        cat.eat()
        cat.sleep()

        self.assertEqual(False, cat.sleepy)

if __name__ == '__main__':
    unittest.main()