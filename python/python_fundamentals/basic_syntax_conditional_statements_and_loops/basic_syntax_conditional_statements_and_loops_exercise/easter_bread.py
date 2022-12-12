budget = float(input())
price_for_1kg_flour = float(input())

price_for_1pack_of_eggs = price_for_1kg_flour * 0.75
price_for_1l_milk = (price_for_1kg_flour * 1.25) * 0.25

needed_money_for_one_loaf = price_for_1l_milk + price_for_1pack_of_eggs + price_for_1kg_flour

loaf_of_bread = 0
colored_eggs = 0

while budget > 0 and budget >= needed_money_for_one_loaf:
        budget -= needed_money_for_one_loaf
        loaf_of_bread += 1
        colored_eggs += 3

        if loaf_of_bread % 3 ==0:
            colored_eggs -= loaf_of_bread - 2

print(f"You made {loaf_of_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
