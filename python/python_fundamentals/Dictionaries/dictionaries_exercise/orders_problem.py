name_price_and_quality = input()

products = {}

while name_price_and_quality != "buy":
    product = name_price_and_quality.split()

    name = product[0]
    price = float(product[1])
    quality = int(product[2])

    if name not in products.keys():
        products[name] = [price, quality]
    else:
        quality_prod = int(products[name][1])
        quality_prod += quality
        products[name][1] = quality_prod
        if price != float(products[name][0]):
            products[name][0] = price

    name_price_and_quality = input()

for prod, total in products.items():
    the_price = total[0]
    the_count = total[1]
    print(f"{prod} -> {the_count * the_price:.2f}")