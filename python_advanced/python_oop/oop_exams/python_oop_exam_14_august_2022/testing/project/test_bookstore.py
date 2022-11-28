import unittest
from project.bookstore import Bookstore


class TestLibrary(unittest.TestCase):
    def test_books_init(self):
        self.bookstore = Bookstore(10)
        self.assertEqual(self.bookstore.books_limit, 10)
        self.assertEqual(self.bookstore.total_sold_books, 0)

        with self.assertRaises(ValueError) as ve:
            self.invalid_bookstore = Bookstore(0)
        self.assertEqual(str(ve.exception), "Books limit of 0 is not valid")

        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book('Title', 11)
        self.assertEqual(str(ex.exception), "Books limit is reached. Cannot receive more books!")

        result = self.bookstore.receive_book("Title", 5)
        self.assertEqual(result, "5 copies of Title are available in the bookstore.")
        self.assertEqual(len(self.bookstore), 5)
        result_second = self.bookstore.receive_book("Title", 5)
        self.assertEqual(result_second, "10 copies of Title are available in the bookstore.")
        self.assertEqual(len(self.bookstore), 10)

        sell_book_example = self.bookstore.sell_book("Title", 2)
        self.assertEqual(sell_book_example, "Sold 2 copies of Title")
        self.assertEqual(len(self.bookstore), 8)
        self.assertEqual(self.bookstore.total_sold_books, 2)
        sell_book_second_example = self.bookstore.sell_book("Title", 8)
        self.assertEqual(sell_book_second_example, "Sold 8 copies of Title")
        self.assertEqual(len(self.bookstore), 0)
        self.assertEqual(self.bookstore.total_sold_books, 10)

        self.assertEqual(str(self.bookstore), "Total sold books: 10\n"
                                              "Current availability: 0\n"
                                              " - Title: 0 copies")

        self.bookstore.receive_book("Title", 8)

        with self.assertRaises(Exception) as ke:
            self.bookstore.sell_book('Invalid', 2)
        self.assertEqual(str(ke.exception), "Book Invalid doesn't exist!")

        with self.assertRaises(Exception) as ve:
            self.bookstore.sell_book('Title', 9)
        self.assertEqual(str(ve.exception), "Title has not enough copies to sell. Left: 8")
