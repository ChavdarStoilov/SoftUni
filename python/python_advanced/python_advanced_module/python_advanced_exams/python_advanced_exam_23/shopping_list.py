def shopping_list(money, **kwargs):
    bought_product = {}
    spend_money = 0
    left_products = len(kwargs)

    if money >= 100:
        for product, quantity in kwargs.items():

            if len(bought_product) == 5:
                break
            elif left_products == 0:
                break

            product_price = quantity[0] * quantity[1]

            if product_price <= money:
                if spend_money + product_price > money:
                    break
                spend_money += product_price
                bought_product[product] = product_price
                left_products -= 1

        result = [f'You bought {prod} for {price:.2f} leva.' for prod, price in bought_product.items()]

        return '\n'.join(result)

    else:
        return 'You do not have enough budget.'



print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
