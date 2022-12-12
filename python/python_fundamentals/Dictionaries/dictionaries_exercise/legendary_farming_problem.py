legendary_items = {"shards": 0, "fragments": 0, "motes": 0}

collected_legendary_item = True

while collected_legendary_item:
    farming = input().split()

    for index in range(0, len(farming), + 2):
        item = farming[index + 1].lower()
        count = int(farming[index])
        if item not in legendary_items:
            legendary_items[item] = count
        else:
            legendary_items[item] += count

        if int(legendary_items["shards"]) >= 250:
            print("Shadowmourne obtained!")
            legendary_items["shards"] -= 250
            collected_legendary_item = False
            break
        elif int(legendary_items["fragments"]) >= 250:
            print("Valanyr obtained!")
            legendary_items["fragments"] -= 250
            collected_legendary_item = False
            break
        elif int(legendary_items["motes"]) >= 250:
            print("Dragonwrath obtained!")
            legendary_items["motes"] -= 250
            collected_legendary_item = False
            break

for items, counts in legendary_items.items():
    print(f"{items}: {counts}")






