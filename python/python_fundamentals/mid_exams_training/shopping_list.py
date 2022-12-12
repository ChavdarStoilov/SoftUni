def shopping_func(the_list):
    command = input()
    while command != "Go Shopping!":
        product = command.split()

        if product[0] == "Urgent":
            if product[1] not in the_list:
                the_list.insert(0, product[1])

        elif product[0] == "Unnecessary":
            if product[1] in the_list:
                the_list.remove(product[1])

        elif product[0] == "Correct":
            if product[1] in the_list:
                for item in range(len(the_list)):
                    if the_list[item] == product[1]:
                        the_list[item] = product[2]
                        break

        elif product[0] == "Rearrange":
            if product[1] in the_list:
                for item_two in range(len(the_list)):
                    if the_list[item_two] == product[1]:
                        the_list.append(the_list[item_two])
                        the_list.pop(item_two)
                        break
        command = input()

    return ", ".join(the_list)

list_for_shopping = input().split("!")
print(shopping_func(list_for_shopping))
