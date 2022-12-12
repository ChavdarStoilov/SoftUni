from project.bookstore import Bookstore

import unittest

class TestBookstore(unittest.TestCase):
    LIMIT = 10

    def test__init(self):
        store = Bookstore(self.LIMIT)

        actual_limit = store.books_limit
        actual_availability_in_store_by_book_titles = store.availability_in_store_by_book_titles
        actual_total_sold_books = store.total_sold_books

        self.assertEqual(self.LIMIT, actual_limit)
        self.assertEqual({}, actual_availability_in_store_by_book_titles)
        self.assertEqual(0, actual_total_sold_books)

    def test__books_setter_with_zero_and_negative__expect_error(self):

        with self.assertRaises(ValueError) as ex:
            Bookstore(0)

        self.assertEqual('Books limit of 0 is not valid', str(ex.exception))

        with self.assertRaises(ValueError) as ex_two:
            Bookstore(-1)

        self.assertEqual('Books limit of -1 is not valid', str(ex_two.exception))


    def test__len_function(self):
        store = Bookstore(self.LIMIT)

        self.assertEqual(0, len(store))

    def test__receiving_books(self):
        store = Bookstore(self.LIMIT)

        with self.assertRaises(Exception) as ex:
            store.receive_book('Star Wars', 20)

        self.assertEqual('Books limit is reached. Cannot receive more books!', str(ex.exception))

        car = store.receive_book('Cars', 5)

        self.assertEqual({'Cars': 5}, store.availability_in_store_by_book_titles)
        self.assertEqual('5 copies of Cars are available in the bookstore.', car)


    def test__selling_books(self):
        store = Bookstore(self.LIMIT)
        store.receive_book('Cars', 5)

        with self.assertRaises(Exception) as ex:
            store.sell_book('StarWars', 2)

        self.assertEqual('Book StarWars doesn\'t exist!', str(ex.exception))

        with self.assertRaises(Exception) as ex_two:
            store.sell_book('Cars', 20)

        self.assertEqual('Cars has not enough copies to sell. Left: 5', str(ex_two.exception))

        sell_cars = store.sell_book('Cars', 2)

        self.assertEqual('Sold 2 copies of Cars', sell_cars)
        self.assertEqual(3, store.availability_in_store_by_book_titles['Cars'])
        self.assertEqual(2, store.total_sold_books)


    def test__str_output(self):
        store = Bookstore(self.LIMIT)
        store.receive_book('Cars', 5)
        store.sell_book('Cars', 2)

        actual = str(store)
        expect = 'Total sold books: 2\n' \
                 'Current availability: 3\n' \
                 ' - Cars: 3 copies'

        self.assertEqual(expect, actual)

if __name__ == '__main__':
    unittest.main()