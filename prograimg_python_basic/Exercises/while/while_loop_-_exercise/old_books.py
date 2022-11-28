favorite_book_name = str(input())

count_checked = 0
is_book_found = False
book_name = str(input())

while book_name != "No More Books":
    if favorite_book_name == book_name:
        is_book_found = True
        print(f"You checked {count_checked} books and found it.")
        break

    count_checked += 1
    book_name = str(input())

if not is_book_found:
    print(f"The book you search is not here! \nYou checked {count_checked} books.")