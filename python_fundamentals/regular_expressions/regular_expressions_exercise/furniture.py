import re

total_sum = 0.0
items = []

some_furniture = input()

while some_furniture != "Purchase":
    pattern = r">>((?P<item>[a-zA-Z]+))<<(?P<price>\d+[.|[\d]+)[!](?P<count>\d+)"

    the_finder = re.finditer(pattern, some_furniture)

    for info in the_finder:
        items.append(info.group("item"))
        quantity = int(info.group("count"))
        price = float(info.group("price"))
        total_sum += price * quantity

    some_furniture = input()


print("Bought furniture:")
for item in items:
    print(f"{item}")

print(f"Total money spend: {total_sum:.2f}")