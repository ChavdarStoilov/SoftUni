def squares(number):
    start_num = 1

    while start_num <= number:
        yield start_num ** 2

        start_num += 1


print(list(squares(5)))	#[1, 4, 9, 16, 25]