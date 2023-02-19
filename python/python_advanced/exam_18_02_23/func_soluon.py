def shop_from_grocery_list(*args):

    budget = args[0]
    products_need_to_buy = args[1]
    products = args[2:]

    for product, price in products:
        if price > budget:
            break

        if product in products_need_to_buy:
            products_need_to_buy.remove(product)
            budget -= price

    if not products_need_to_buy:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(products_need_to_buy)}."

print(shop_from_grocery_list(
    5,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))



print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
