first_number = int(input())
second_number = int(input())

end_step = first_number * second_number
list_for_numbers = []

for number in range(end_step, first_number -1, -1):
    if number % first_number == 0:
        list_for_numbers.append(number)


list_for_numbers.reverse()
print(list_for_numbers)