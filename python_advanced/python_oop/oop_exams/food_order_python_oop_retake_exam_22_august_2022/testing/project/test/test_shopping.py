import unittest
from project.shopping_cart import ShoppingCart


class TestShoppingCart(unittest.TestCase):

    def test__init(self):
        shop_cart = ShoppingCart('Cooks', 2000)

        actual_name = shop_cart.shop_name
        actual_budget = shop_cart.budget
        actual_products = shop_cart.products

        self.assertEqual('Cooks', actual_name)
        self.assertEqual(2000, actual_budget)
        self.assertEqual({}, actual_products)

        with self.assertRaises(ValueError) as ex:
            shop_cart_two = ShoppingCart('cookie', 1000)

        self.assertEqual('Shop must contain only letters and must start with capital letter!', str(ex.exception))


    def test__adding_to_card(self):
        shop_cart = ShoppingCart('Cookie', 2000)

        actual_added = shop_cart.add_to_cart('cookie', 50)
        actual_products = shop_cart.products

        self.assertEqual('cookie product was successfully added to the cart!', actual_added)
        self.assertEqual({'cookie': 50}, actual_products)

        shop_cart_two = ShoppingCart('Jonny', 10)
        with self.assertRaises(ValueError) as ex:
            shop_cart_two.add_to_cart('pony', 110)

        self.assertEqual('Product pony cost too much!', str(ex.exception))

    def test__remove_from_cart(self):
        shop_cart = ShoppingCart('Jonny', 1000)
        shop_cart.add_to_cart('cookies', 20)
        shop_cart.add_to_cart('cake', 60)
        actual_removed = shop_cart.remove_from_cart('cake')
        actual_left_products = shop_cart.products

        self.assertEqual('Product cake was successfully removed from the cart!', actual_removed)
        self.assertEqual({'cookies': 20}, actual_left_products)

        with self.assertRaises(ValueError) as ev:
            shop_cart.remove_from_cart('cake')

        self.assertEqual('No product with name cake in the cart!', str(ev.exception))


    def test__adding_dunder(self):
        shop_cart_one = ShoppingCart('Jonny', 2000)
        shop_cart_two = ShoppingCart('Deep', 100)
        shop_cart_one.add_to_cart('cookies', 20)
        shop_cart_one.add_to_cart('cake', 30)
        shop_cart_two.add_to_cart('pizza', 20)

        new_shop = shop_cart_one + shop_cart_two
        actual_name = new_shop.shop_name
        actual_budget = new_shop.budget
        actual_products = new_shop.products

        expect_products = {
            'cookies': 20,
            'cake': 30,
            'pizza': 20
        }
        self.assertEqual('JonnyDeep', actual_name)
        self.assertEqual(2100, actual_budget)
        self.assertEqual(expect_products, actual_products)


    def test__buy_product(self):
        shop_cart = ShoppingCart('Oho', 100)
        shop_cart.add_to_cart('pizza', 20)
        shop_cart.add_to_cart('cookies', 30)
        shop_cart.add_to_cart('cola', 10)
        
        actual_buying = shop_cart.buy_products()
        
        self.assertEqual('Products were successfully bought! Total cost: 60.00lv.', actual_buying)

        shop_cart.add_to_cart('Burger', 50)
        with self.assertRaises(ValueError) as ex:
            shop_cart.buy_products()

        self.assertEqual('Not enough money to buy the products! Over budget with 10.00lv!', str(ex.exception))