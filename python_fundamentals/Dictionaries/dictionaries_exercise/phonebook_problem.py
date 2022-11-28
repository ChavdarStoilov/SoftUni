name_and_number = input()
count_search = 0
phone_book = {}

while True:
    if "-" not in name_and_number:
        count_search = int(name_and_number)
        break

    names_and_numbers = name_and_number.split("-")

    phone_book[names_and_numbers[0]] = names_and_numbers[1]


    name_and_number = input()

for _ in range(count_search):
    name = input()

    if name in phone_book.keys():
        print(f"{name} -> {phone_book.get(name)}")
    else:
        print(f"Contact {name} does not exist.")

