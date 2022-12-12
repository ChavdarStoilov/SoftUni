some_string_of_integers = str(input()).split(", ")
count_of_beggars = int(input())

list_of_count_beggars = []
sum_of_beggars = 0
beggars_counter = 0

for _ in range(count_of_beggars):
    for index in range(beggars_counter, len(some_string_of_integers), count_of_beggars):
        sum_of_beggars += int(some_string_of_integers[index])

    beggars_counter += 1
    list_of_count_beggars.append(sum_of_beggars)
    sum_of_beggars = 0

print(list_of_count_beggars)