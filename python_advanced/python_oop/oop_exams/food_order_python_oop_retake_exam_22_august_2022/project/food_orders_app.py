from project.client import Client


# 13:10 - start
class FoodOrdersApp:
    RECEIPT_ID = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):

        for clients in self.clients_list:
            if clients.phone_number == client_phone_number:
                raise Exception('The client has already been registered!')

        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f'Client {client_phone_number} registered successfully.'

    def add_meals_to_menu(self, *meals):

        for meal in meals:
            if meal.__class__.__name__ in ('Starter', 'MainDish', 'Dessert'):
                self.menu.append(meal)

    def show_menu(self):
        result = []

        if len(self.menu) < 5:
            raise Exception('The menu is not ready!')

        for meal in self.menu:
            result.append(meal.details())

        return '\n'.join(result)

    def check_clients(self, number):

        for client in self.clients_list:
            if client.phone_number == number:
                return client

        client = Client(number)
        self.clients_list.append(client)
        return client

    def check_meals(self, meal):

        for meals in self.menu:
            if meals.name == meal and meals.__class__.__name__ in ('Starter', 'MainDish', 'Dessert'):
                return meals

        return False

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        client = self.check_clients(client_phone_number)

        if len(self.menu) < 5:
            raise Exception('The menu is not ready!')

        for meals, quantity in meal_names_and_quantities.items():
            meal = self.check_meals(meals)

            if not meal:
                raise Exception(f'{meals} is not on the menu!')

            if meal.quantity < quantity:
                raise Exception('Not enough quantity of {meal_type}: {meal_name}!')

            client.shopping_cart.append(meal)
            client.ordered_meals[meals] = quantity
            meal.quantity -= quantity
            price = meal.price * quantity
            client.bill += price

        added_meals_name = [meal.name for meal in client.shopping_cart]
        return f'Client {client_phone_number} successfully ordered {", ".join(added_meals_name)} for {client.bill:.2f}lv.'

    def cancel_order(self, client_phone_number: str):
        client = self.check_clients(client_phone_number)

        if not client.shopping_cart:
            raise Exception('There are no ordered meals!')

        client.bill = 0.0
        for meal, quantity in client.ordered_meals.items():
            for meals in client.shopping_cart:
                if meals.name == meal:
                    meals.quantity += quantity

        client.shopping_cart = []


        return f'Client {client_phone_number} successfully canceled his order.'

    def finish_order(self, client_phone_number: str):
        client = self.check_clients(client_phone_number)

        if not client.shopping_cart:
            raise Exception('There are no ordered meals!')

        self.RECEIPT_ID += 1
        client.shopping_cart = []
        bill = client.bill
        client.bill = 0
        return f'Receipt #{self.RECEIPT_ID} with total amount of {bill:.2f} was successfully paid for {client_phone_number}.'

    def __str__(self):

        return f'Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients.'
