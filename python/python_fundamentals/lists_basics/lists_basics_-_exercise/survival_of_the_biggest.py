some_numbers = str(input())
count_of_remove = int(input())

list_of_the_numbers = some_numbers.split(" ")
list_number = []

for number in list_of_the_numbers:
    list_number.append(int(number))

list_of_the_numbers.clear()


for _ in range(count_of_remove):
    min_num = min(list_number)
    list_number.remove(min_num)

for num in list_number:
    list_of_the_numbers.append(str(num))


print(", ".join(list_of_the_numbers))