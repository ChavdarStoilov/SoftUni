product_dict = {}

command = input()

while command != "statistics":
    product = command.split(":")

    if product[0] not in product_dict.keys():
        product_dict[product[0]] = int(product[1])
    else:
        product_dict[product[0]] += int(product[1])

    command = input()


print("Products in stock:")
for (prod, count) in product_dict.items():
    print(f"- {prod}: {count}")
print(f"Total Products: {len(product_dict)}\n"
      f"Total Quantity: {sum(product_dict.values())}")