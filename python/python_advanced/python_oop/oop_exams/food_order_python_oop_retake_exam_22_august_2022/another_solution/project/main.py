# Food Orders cancel order successfully
import unittest
from project.food_orders_app import FoodOrdersApp
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.starter import Starter


class TestFoodOrdersAppClass(unittest.TestCase):
    def test_add_meals_method(self):
        self.foa = FoodOrdersApp()

        dessert = Dessert('cake', 10)
        main_dish = MainDish('fish', 12)
        starter = Starter('salad', 11.50)
        second_dessert = Dessert('ice cream', 15, 2)
        second_main_dish = MainDish('pizza', 18.90, 8)
        self.foa.add_meals_to_menu(dessert, main_dish, starter, second_dessert, second_main_dish)

        self.foa.add_meals_to_shopping_cart('0123456789', **{'cake': 3})
        result = self.foa.cancel_order('0123456789')
        self.assertEqual(result, "Client 0123456789 successfully canceled his order.")
        client = self.foa.clients_list[0]
        self.assertEqual(dessert.quantity, 30)
        self.assertEqual(client.shopping_cart, [])
        self.assertEqual(client.bill, 0)


if __name__ == '__main__':
    unittest.main()