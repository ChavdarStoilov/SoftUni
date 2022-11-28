def shopping_cart(*args):
    meals = {'Pizza': [], 'Soup': [], 'Dessert': []}

    for meal in args:

        if meal == 'Stop':
            break

        if meal[0] == 'Pizza' and len(meals['Pizza']) == 4:
            continue
        elif meal[0] == 'Soup' and len(meals['Soup']) == 3:
            continue
        elif meal[0] == 'Dessert' and len(meals['Dessert']) == 2:
            continue

        if meal[1] not in meals[meal[0]]:
            meals[meal[0]].append(meal[1])

    count_products = [len(product) for product in meals.values()]
    if sum(count_products) == 0:
        return 'No products in the cart!'

    sorted_meals = sorted(meals.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ''
    for tuple_ in sorted_meals:
        result += f"{tuple_[0]}:\n"
        sorted_product = sorted(tuple_[1])
        for product in sorted_product:
            result += f" - {product}\n"

    return result

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

