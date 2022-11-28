list_of_numbers = input().split(", ")

end_list = []
counter = 0

for index_number in range(len(list_of_numbers)):
    if int(list_of_numbers[index_number]) == 0:
        end_list.append(int(list_of_numbers[index_number]))
    else:
        end_list.insert(counter, int(list_of_numbers[index_number]))
        counter += 1

print(end_list)