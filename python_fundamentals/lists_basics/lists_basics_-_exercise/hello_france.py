collection_of_items = input().split("|")
budget = float(input())

list_price_of_bought_items = []
profit = 0
cost_money = 0

for prices in collection_of_items:
    product_and_prices = prices.split("->")

    type_of_product = product_and_prices[0]
    the_price_of_product = float(product_and_prices[1])

    if budget < the_price_of_product:
        continue

    if type_of_product == "Clothes" and the_price_of_product <= 50:
        budget -= the_price_of_product
        new_price = the_price_of_product * 1.4
        list_price_of_bought_items.append(new_price)
        cost_money += the_price_of_product

    elif type_of_product == "Shoes" and the_price_of_product <= 35:
        budget -= the_price_of_product
        new_price = the_price_of_product * 1.4
        list_price_of_bought_items.append(new_price)
        cost_money += the_price_of_product

    elif "Accessories" and the_price_of_product <= 20.5:
        budget -= the_price_of_product
        new_price = the_price_of_product * 1.4
        list_price_of_bought_items.append(new_price)
        cost_money += the_price_of_product

profit = sum(list_price_of_bought_items) - cost_money

for price in list_price_of_bought_items:
    print(f"{price:.2f}", end=" ")


print(f"\nProfit: {profit:.2f}")

if sum(list_price_of_bought_items) + budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
print(sum(list_price_of_bought_items) + budget)
# 189.12600000000003