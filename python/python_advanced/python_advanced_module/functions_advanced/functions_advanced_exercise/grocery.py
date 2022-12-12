def grocery_store(**kwargs):
    products = []

    sorted_by_quantity = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    for product in sorted_by_quantity:
        name = product[0]
        quantity = product[1]
        products.append(f'{name}: {quantity}')


    return '\n'.join(products)

print(grocery_store(
    bread=5,
    pasta=12,
    eggss=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
