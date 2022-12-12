shop = {}
sold_food = 0

while True:
    commands = input().split()
    command = commands[0]

    if command == 'Complete':
        break

    quantity = int(commands[1])
    food = commands[2]


    if command == 'Receive':
        if quantity > 0:
            if food not in shop.keys():
                shop[food] = 0
            shop[food] += quantity

    elif command == 'Sell':
        if food in shop.keys():
            if shop[food] < quantity:
                sold_quantity = shop[food]
                sold_food += sold_quantity
                del shop[food]
                print(f"There aren't enough {food}. You sold the last {sold_quantity} of them.")
            else:
                shop[food] -= quantity
                sold_food += quantity
                print(f"You sold {quantity} {food}.")
                if shop[food] <= 0:
                    del shop[food]

        else:
            print(f"You do not have any {food}.")

for key, value in shop.items():
    print(f"{key}: {value}")

print(f"All sold: {sold_food} goods")


