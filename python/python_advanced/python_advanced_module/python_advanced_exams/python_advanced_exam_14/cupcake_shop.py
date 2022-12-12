from collections import deque


def stock_availability(inventory, action,  *args):
    inventory = deque(inventory)

    if action == 'delivery':
        for product in args:
            inventory.append(product)

    elif action == 'sell':
        if len(args) == 0:
            inventory.popleft()
        else:
            for products in args:
                if isinstance(products, int):
                    for _ in range(products):
                        inventory.popleft()
                else:
                    if products in inventory:
                        count_product = inventory.count(products)
                        for _ in range(count_product):
                            inventory.remove(products)

    return list(inventory)

print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
