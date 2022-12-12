command = input()

the_book = {}

while command != "Lumpawaroo":
    check = False
    if " | " in command:
        power_and_name = command.split(" | ")
        if power_and_name[0] not in the_book:
            the_book[power_and_name[0]] = []

            print(the_book.values())
        for team, user in the_book.items():
            if power_and_name[1] in user:
                break
            the_book[power_and_name[0]].append(power_and_name[1])


    elif " -> " in command:
        power_and_name = command.split(" -> ")
        if power_and_name[1] not in the_book:
            the_book[power_and_name[1]] = []
        for the_power, the_name in the_book.items():
            if power_and_name[0] in the_name:
                name = "".join(the_name)
                the_book[the_power].remove(name)
                break

        the_book[power_and_name[1]].append(power_and_name[0])
        print(f"{power_and_name[0]} joins the Lighter side!")

    command = input()

for side, names in the_book.items():
    if len(names) > 0:
        print(f"Side: {side}, Members: {len(names)}")
        for name in names:
            print(f"! {name}")

# Light | Peter
# Light | Peter
# Light | Peter
# Dark | Kim
# Dark | sss
# Dark | Kim
# Light | Kim
# Light | aa
# Light | Kibm
# Lumpawaroo
