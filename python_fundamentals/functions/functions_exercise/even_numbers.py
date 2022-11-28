some_number = input().split()

lists = []
def even_number(num):
    if int(num) % 2 == 0:
        return True

the_filter = list(filter(even_number, some_number))

for number in the_filter:
    lists.append(int(number))

print(lists)
