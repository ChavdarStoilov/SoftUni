from project.hero import Hero
import unittest

class TestHero(unittest.TestCase):
    USERNAME = 'fifa'
    LEVEL = 10
    HEALTH = 1000
    DAMAGE = 20

    def test__checking_init(self):
        hero = Hero(self.USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)

        self.assertEqual(self.USERNAME, hero.username)
        self.assertEqual(self.LEVEL, hero.level)
        self.assertEqual(self.HEALTH, hero.health)
        self.assertEqual(self.DAMAGE, hero.damage)

    def test__enemy_hero_cannot_be_the_same_as_hero_username__expect_raise_error(self):
        hero = Hero(self.USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)
        hero_enemy = Hero(self.USERNAME, 10, 100, 40)

        with self.assertRaises(Exception) as ex:
            hero.battle(hero_enemy)

        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test__hero_cannot_be_with_zero_or_negative_health__expect_raise_error(self):
        hero = Hero(self.USERNAME, self.LEVEL, 0, self.DAMAGE)
        hero_enemy = Hero('Jonny', 10, 100, 40)

        with self.assertRaises(Exception) as ex:
            hero.battle(hero_enemy)

        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

        hero = Hero(self.USERNAME, self.LEVEL, -1, self.DAMAGE)

        with self.assertRaises(Exception) as ex:
            hero.battle(hero_enemy)

        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

    def test__enemy_hero_cannot_be_with_zero_or_negative_health__expect_raise_error(self):
        hero = Hero(self.USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)
        hero_enemy = Hero('Jonny', 10, 0, 40)

        with self.assertRaises(Exception) as ex:
            hero.battle(hero_enemy)

        self.assertEqual('You cannot fight Jonny. He needs to rest', str(ex.exception))

        hero_enemy_two = Hero('Jonny', 10, -1, 40)

        with self.assertRaises(Exception) as ex:
            hero.battle(hero_enemy)

        self.assertEqual('You cannot fight Jonny. He needs to rest', str(ex.exception))


    def test__hero_damage_and_enemy_damage_and_decrease_healths(self):
        hero = Hero(self.USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)
        hero_enemy = Hero('Jonny', 10, 800, 40)

        hero.battle(hero_enemy)

        hero_damage = self.DAMAGE * self.LEVEL
        enemy_damage = 40 * 10

        actual_hero_health = hero.health
        actual_enemy_health = hero_enemy.health

        except_hero_health = self.HEALTH - enemy_damage
        except_enemy_health = 800 - hero_damage


        self.assertEqual(except_hero_health, actual_hero_health)
        self.assertEqual(except_enemy_health, except_enemy_health)

    def test__draw_result_after_battle(self):
        hero = Hero(self.USERNAME, self.LEVEL, 100, self.DAMAGE)
        hero_enemy = Hero('Jonny', 10, 100, 40)

        actual = hero.battle(hero_enemy)

        self.assertEqual('Draw', actual)

    def test__hero_win_after_battle__expect_level_up_health_increase_damage_increase(self):
        hero = Hero(self.USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)
        hero_enemy = Hero('Jonny', 10, 100, 40)


        actual_result = hero.battle(hero_enemy)
        health_hero_after_battle = self.HEALTH - 40 * 10
        actual_level = hero.level
        actual_health = hero.health
        actual_damage = hero.damage


        expect_level = self.LEVEL + 1
        expect_health = health_hero_after_battle + 5
        expect_damage = self.DAMAGE + 5

        self.assertEqual(expect_level, actual_level)
        self.assertEqual(expect_health, actual_health)
        self.assertEqual(expect_damage, actual_damage)
        self.assertEqual('You win', actual_result)


    def test__enemy_win_after_battle__expect_level_up_health_increase_damage_increase(self):
        hero = Hero(self.USERNAME, self.LEVEL, 100, self.DAMAGE)
        hero_enemy = Hero('Jonny', 10, 1000, 40)


        actual_result = hero.battle(hero_enemy)
        health_hero_after_battle = 1000 - 20 * 10
        actual_level = hero_enemy.level
        actual_health = hero_enemy.health
        actual_damage = hero_enemy.damage


        expect_level = 10 + 1
        expect_health = health_hero_after_battle + 5
        expect_damage = 40 + 5

        self.assertEqual(expect_level, actual_level)
        self.assertEqual(expect_health, actual_health)
        self.assertEqual(expect_damage, actual_damage)
        self.assertEqual('You lose', actual_result)

    def test__end_result_str_function(self):
        hero = Hero(self.USERNAME, self.LEVEL, 1000, self.DAMAGE)
        hero_enemy = Hero('Jonny', 10, 100, 40)

        hero.battle(hero_enemy)
        health_hero_after_battle = self.HEALTH - 40 * 10
        actual = str(hero)

        self.LEVEL += 1
        self.HEALTH = health_hero_after_battle + 5
        self.DAMAGE += 5


        expect = f"Hero {self.USERNAME}: {self.LEVEL} lvl\n" \
                 f"Health: {self.HEALTH}\n" \
                 f"Damage: {self.DAMAGE}\n"

        self.assertEqual(expect, actual)

if __name__ == '__main__':
    unittest.main()

