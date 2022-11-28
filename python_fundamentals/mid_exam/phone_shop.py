def shop(phones):

    command = input()

    while command != "End":
        action = command.split(" - ")

        if action[0] == "Add":
            if action[1] not in phones:
                phones.append(action[1])

        elif action[0] == "Remove":
            if action[1] in phones:
                phones.remove(action[1])

        elif action[0] == "Bonus phone":
            bonus = action[1].split(":")
            if bonus[0] in phones:
                index = phones.index(bonus[0])
                phones.insert(index +1, bonus[1])

        elif action[0] == "Last":
            if action[1] in phones:
                phones.remove(action[1])
                phones.append(action[1])

        command = input()

    return f"{', '.join(phones)}"


list_of_phones = input().split(", ")

print(shop(list_of_phones))