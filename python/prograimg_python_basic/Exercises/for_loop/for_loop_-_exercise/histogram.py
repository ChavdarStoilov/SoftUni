count_of_number = int(input())

first_numbers = 0
second_numbers = 0
third_numbers = 0
fourth_numbers = 0
fifth_numbers = 0

for numbers in range(count_of_number):
    number = int(input())
    if number < 200:
        first_numbers += 1
    elif 200 <= number <= 399:
        second_numbers += 1
    elif 400 <= number <= 599:
        third_numbers += 1
    elif 600 <= number <= 799:
        fourth_numbers += 1
    else:
        fifth_numbers += 1


first_percentage = first_numbers / count_of_number * 100
second_percentage = second_numbers / count_of_number * 100
third_percentage = third_numbers / count_of_number * 100
fourth_percentage = fourth_numbers / count_of_number * 100
fifth_percentage = fifth_numbers / count_of_number * 100

print(f"{first_percentage:.2f}% \n{second_percentage:.2f}% \n{third_percentage:.2f}% \n{fourth_percentage:.2f}%"
      f"\n{fifth_percentage:.2f}%")