from project.toy_store import ToyStore
import unittest


class ToyStoreTest(unittest.TestCase):

    def test__init_pams(self):
        store = ToyStore()

        actual = store.toy_shelf
        expect = {"A": None,
                  "B": None,
                  "C": None,
                  "D": None,
                  "E": None,
                  "F": None,
                  "G": None,
                  }

        self.assertEqual(expect, actual)

    def test__adding_shelf_not_in_list_toy_in_store__expect_error(self):
        store = ToyStore()

        with self.assertRaises(Exception) as ex:
            store.add_toy('Q', 'truck')

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))


    def test__adding_toy_that_already_exits__expect_error(self):
        store = ToyStore()

        added = store.add_toy('A', 'truck')

        self.assertEqual("Toy:truck placed successfully!", added)

        with self.assertRaises(Exception) as ex:
            store.add_toy('A', 'truck')

        self.assertEqual("Toy is already in shelf!", str(ex.exception))


    def test__adding_toy_on_shelf_taken__expect_error(self):
        store = ToyStore()

        added = store.add_toy('A', 'truck')
        self.assertEqual("Toy:truck placed successfully!", added)
        self.assertEqual('truck', store.toy_shelf['A'])

        with self.assertRaises(Exception) as ex:
            store.add_toy('A', 'car')

        self.assertEqual("Shelf is already taken!", str(ex.exception))


    def test__remove_toy_that_shelf_not_exit__expect_error(self):
        store = ToyStore()

        with self.assertRaises(Exception) as ex:
            store.remove_toy('Q', 'car')

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test__remove_toy_that_not_exit__expect_error(self):
        store = ToyStore()
        store.add_toy('A', 'truck')

        with self.assertRaises(Exception) as ex:
            store.remove_toy('A', 'car')

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))


    def test__remove_successfully(self):
        store = ToyStore()
        store.add_toy('A', 'truck')

        removed = store.remove_toy('A', 'truck')

        self.assertEqual("Remove toy:truck successfully!", removed)
        self.assertEqual(None, store.toy_shelf['A'])



if __name__ == "__main__":
    unittest.main()
