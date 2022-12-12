from testing.testing_lab.scripts.extended_list import IntegerList

import unittest


class TestIntegerList(unittest.TestCase):

    def test_types_of_element_in_list__expect_all_to_be_integer(self):
        lister = IntegerList(1, 2, 3, 'i')
        actually = lister.get_data()
        expect = [1, 2, 3]

        self.assertEqual(expect, actually)

    def test_adding_element_in_the_list__expect_added_element_and_raise_error_if_value_not_int(self):
        lister = IntegerList(1, 2)
        lister.add(3)
        actually = lister.get_data()
        expect = [1, 2, 3]

        with self.assertRaises(Exception) as ex:
            lister.add('a')

        self.assertIsNotNone(ex)
        self.assertEqual(expect, actually)

    def test_removing_element_from_list_by_idx__expect_raise_if_out_of_range(self):
        lister = IntegerList(1, 2, 3)
        lister.remove_index(0)
        actually = lister.get_data()
        expect = [2, 3]

        with self.assertRaises(Exception) as ex:
            lister.remove_index(5)

        self.assertIsNotNone(ex)
        self.assertEqual(expect, actually)

    def test_testing_get_function__expect_get_element_by_index__or_raise_index_err(self):
        lister = IntegerList(1, 2, 3)
        actually = lister.get(1)
        expect = 2

        with self.assertRaises(Exception) as ex:
            lister.get(4)

        self.assertIsNotNone(ex)
        self.assertEqual(expect, actually)

    def test_insert_function__expect_add_new_element_in_provided_idx__or_raise_out_of_range__or_type_error(self):
        lister = IntegerList(1, 2, 3, 4, 5)
        lister.insert(0, 1)
        actually = lister.get_data()
        expect = [1, 1, 2, 3, 4, 5]

        with self.assertRaises(Exception) as ex:
            lister.insert(7, 2)


        with self.assertRaises(Exception) as ex_two:
            lister.insert(0, 'i')


        self.assertIsNotNone(ex)
        self.assertIsNotNone(ex_two)
        self.assertEqual(expect, actually)

    def test__get_biggest_element_from_list(self):
        lister = IntegerList(1, 2, 3, 10)
        actually = lister.get_biggest()
        expect = 10

        self.assertEqual(expect, actually)

    def test__get_the_index_from_list_by_provided_element(self):
        lister = IntegerList(1, 2, 5)
        actually = lister.get_index(5)
        expect = 2

        self.assertEqual(expect, actually)

if __name__ == '__main__':
    unittest.main()
