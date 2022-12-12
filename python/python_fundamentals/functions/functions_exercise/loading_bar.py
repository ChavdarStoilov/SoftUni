def loading_bar(number):
    loaded = ["["]
    index_number = number // 10

    for idx in range(1, 11):

        if idx <= index_number:
            loaded.insert(idx, "%")
        else:
            loaded.insert(idx, ".")

        if idx == 10:
            loaded.append("]")

    if index_number < 10:
        return f"{number}% {''.join(loaded)}\n"\
               f"Still loading..."
    else:
        return f"100% Complete!\n"\
               f"{''.join(loaded)}"

some_numer = int(input())
print(loading_bar(some_numer))