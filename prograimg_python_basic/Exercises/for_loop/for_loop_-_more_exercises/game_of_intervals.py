count_of_moves = int(input())

result = 0
between_nine = 0
between_nineteen = 0
between_twenty_nine = 0
between_thirty_nine = 0
between_fifty = 0
invalid_numbers = 0

for game in range(0, count_of_moves):
    some_number = int(input())

    if 0 <= some_number <= 9:
        result += some_number * 0.20
        between_nine += 1
    elif 10 <= some_number <= 19:
        result += some_number * 0.30
        between_nineteen += 1
    elif 20 <= some_number <= 29:
        result += some_number * 0.40
        between_twenty_nine += 1
    elif 30 <= some_number <= 39:
        result += 50
        between_thirty_nine += 1
    elif 40 <= some_number <= 50:
        result += 100
        between_fifty += 1
    else:
        invalid_numbers += 1
        result = result / 2


perg_between_nine = (between_nine / count_of_moves) * 100
perg_between_nineteen = (between_nineteen / count_of_moves) * 100
perg_between_twenty_nine = (between_twenty_nine / count_of_moves) * 100
perg_between_thirty_nine = (between_thirty_nine / count_of_moves) * 100
perg_between_fifty = (between_fifty / count_of_moves) * 100
perg_invalid_numbers = (invalid_numbers / count_of_moves) * 100

print(f"{result:.2f}\n"
      f"From 0 to 9: {perg_between_nine:.2f}%\n"
      f"From 10 to 19: {perg_between_nineteen:.2f}%\n"
      f"From 20 to 29: {perg_between_twenty_nine:.2f}%\n"
      f"From 30 to 39: {perg_between_thirty_nine:.2f}%\n"
      f"From 40 to 50: {perg_between_fifty:.2f}%\n"
      f"Invalid numbers: {perg_invalid_numbers:.2f}%")