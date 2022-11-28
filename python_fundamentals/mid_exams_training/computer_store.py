def new_computer(some_price):
    sum_without_tax = 0
    while not (some_price == "special" or some_price == "regular"):

        price = float(some_price)


        if price < 0:
            print("Invalid price!")

        else:
            sum_without_tax += price

        some_price = input()

    tax = sum_without_tax * 0.20
    end_sum = sum_without_tax + tax

    if some_price == "special":
        end_sum = end_sum - (end_sum * 0.10)

    if end_sum == 0:
        return "Invalid order!"

    else:
        return f"Congratulations you've just bought a new computer!\n" \
               f"Price without taxes: {sum_without_tax:.2f}$\n" \
               f"Taxes: {tax:.2f}$\n" \
               f"-----------\n" \
               f"Total price: {end_sum:.2f}$\n"




prices = input()

print(new_computer(prices))
