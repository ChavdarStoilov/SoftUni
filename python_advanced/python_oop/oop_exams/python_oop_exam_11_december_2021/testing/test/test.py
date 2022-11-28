from project.team import Team

import unittest

class TestTeam(unittest.TestCase):
    NAME = 'Real'

    def setUp(self) -> None:
        self.team = Team(self.NAME)

    def test__init(self):

        actual_name = self.team.name
        actual_members = self.team.members

        self.assertEqual(self.NAME, actual_name)
        self.assertEqual({}, actual_members)

    def test__name_property__expect_error(self):

        with self.assertRaises(ValueError) as ex:
            team = Team("12")

        self.assertEqual('Team Name can contain only letters!', str(ex.exception))
        self.assertEqual(self.NAME, self.team.name)

    def test__add_members_function(self):

        actual_added_numbers = self.team.add_member(Gerry= 20, Jonny= 25)

        actual_numbers = self.team.members

        self.assertEqual({'Gerry': 20, 'Jonny': 25}, actual_numbers)
        self.assertEqual('Successfully added: Gerry, Jonny', actual_added_numbers)


    def test__remove_numbers_function(self):
        self.team.add_member(Gerry=20, Jonny=25)
        actual_remove = self.team.remove_member('Gerry')

        self.assertEqual('Member Gerry removed', actual_remove)

        actual_remove = self.team.remove_member('Jessy')

        self.assertEqual('Member with name Jessy does not exist', actual_remove)

    def test__great_then_function(self):
        self.team.add_member(Gerry=20, Jonny=25)
        team_two = Team('ManUnited')
        team_two.add_member(Jessy = 26)

        actual_true = self.team > team_two
        actual_false = self.team < team_two

        self.assertEqual(True, actual_true)
        self.assertEqual(False, actual_false)

    def test__len_of_numbers(self):
        self.team.add_member(Gerry=20, Jonny=25)
        actual = len(self.team)

        self.assertEqual(2, actual)

    def test__adding_function(self):
        self.team.add_member(Gerry=20, Jonny=25)
        team_two = Team('ManUnited')
        team_two.add_member(Jessy=26)

        new_team = self.team + team_two

        actual_new_team_name = new_team.name
        actual_new_team_members = new_team.members


        self.assertEqual(f'{self.NAME}{"ManUnited"}', actual_new_team_name)
        self.assertEqual({"Gerry": 20, "Jonny": 25, "Jessy": 26}, actual_new_team_members)
        self.assertEqual('Team name: RealManUnited\n'
                         'Member: Jessy - 26-years old\n'
                         'Member: Jonny - 25-years old\n'
                         'Member: Gerry - 20-years old', str(new_team))

    def test__str_output(self):
        self.team.add_member(Gerry=20, Jonny=25)

        actual = str(self.team)
        expect = f'Team name: {self.NAME}\nMember: Jonny - 25-years old\nMember: Gerry - 20-years old'

        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()