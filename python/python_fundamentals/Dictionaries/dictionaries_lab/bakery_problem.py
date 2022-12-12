class Bakery:

    def __init__(self, product):
        product_dict = {}
        for i in range(0, len(product), 2):
            product_dict[product[i]] = int(product[i + 1])

        print(product_dict)





some_products = input().split()
products = Bakery(some_products)