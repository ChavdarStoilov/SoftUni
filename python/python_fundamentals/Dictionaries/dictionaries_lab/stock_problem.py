def stock_func(product, needed):
    product_dict = {product[i]: product[i +1] for i in range(0, len(product), 2)}

    for need in needed:
        if need in product_dict.keys():
            print(f"We have {product_dict.get(need)} of {need} left")
        else:
            print(f"Sorry, we don't have {need}")






products = input().split()
needed_product = input().split()
stock_func(products, needed_product)