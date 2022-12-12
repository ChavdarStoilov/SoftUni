from project.movie import Movie

import unittest


class TestMove(unittest.TestCase):
    NAME = 'FEAR'
    YEAR = 2000
    RATING = 5

    def test__init(self):
        movie = Movie(self.NAME, self.YEAR, self.RATING)

        actual_name = movie.name
        actual_year = movie.year
        actual_rating = movie.rating
        actual_actors = movie.actors

        self.assertEqual(self.NAME, actual_name)
        self.assertEqual(self.YEAR, actual_year)
        self.assertEqual(self.RATING, actual_rating)
        self.assertEqual([], actual_actors)

    def test__name_property__expect_error(self):
        with self.assertRaises(ValueError) as ex:
            movie = Movie('', self.YEAR, self.RATING)

        self.assertEqual('Name cannot be an empty string!', str(ex.exception))

    def test__year_property__expect_error(self):
        with self.assertRaises(ValueError) as ex:
            movie = Movie('Fast and F', 1885, self.RATING)

        self.assertEqual('Year is not valid!', str(ex.exception))

    def test__adding_actor(self):
        movie = Movie(self.NAME, self.YEAR, self.RATING)

        movie.add_actor('Jonny')
        actual = movie.add_actor('Jonny')

        self.assertEqual('Jonny is already added in the list of actors!', actual)

    def test__movies_with_is_better(self):
        movie = Movie(self.NAME, self.YEAR, self.RATING)
        movie_two = Movie('Friends', 1999, 10)
        movie_tree = Movie('Saw', 1998, 12)

        actual_one = movie_two > movie_tree
        actual_two = movie_two > movie

        self.assertEqual('"Friends" is better than "FEAR"', actual_two)
        self.assertEqual('"Saw" is better than "Friends"', actual_one)

    def test__repr_function(self):
        movie = Movie(self.NAME, self.YEAR, self.RATING)

        movie.add_actor('Jonny')
        movie.add_actor('Jessy')

        expect = f"Name: {self.NAME}\n" \
                 f"Year of Release: {self.YEAR}\n" \
                 f"Rating: {self.RATING:.2f}\n" \
                 f"Cast: Jonny, Jessy"

        self.assertEqual(expect, movie.__repr__())