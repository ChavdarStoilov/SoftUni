from project.mammal import Mammal

import unittest

class TestMammal(unittest.TestCase):
    def test__init_information(self):
        mammal = Mammal('Jonny', 'ch', 'ku-ku')

        self.assertEqual('Jonny', mammal.name)
        self.assertEqual('ch', mammal.type)
        self.assertEqual('ku-ku', mammal.sound)


    def test__make_sound_function(self):
        mammal = Mammal('Jonny', 'ch', 'ku-ku')
        actually = mammal.make_sound()
        expect = 'Jonny makes ku-ku'

        self.assertEqual(expect, actually)

    def test__get_kingdom_function(self):
        mammal = Mammal('Jonny', 'ch', 'ku-ku')


        self.assertEqual('animals', mammal.get_kingdom())

    def test__get_info_function(self):
        mammal = Mammal('Jonny', 'ch', 'ku-ku')

        actually = mammal.info()
        expect = 'Jonny is of type ch'

        self.assertEqual(expect, actually)
