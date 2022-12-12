def orders(type_order, quantity):
    end_result = 0

    if type_order == "coffee":
        end_result = quantity * 1.50
    elif type_order == "coke":
        end_result = quantity * 1.40
    elif type_order == "water":
        end_result = quantity * 1.00
    elif type_order == "snacks":
        end_result = quantity * 2.00

    return f"{end_result:.2f}"

order = str(input())
quantity = int(input())

print(orders(order, quantity))