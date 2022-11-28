number_of_names = int(input())

unique_names = set()

for _ in range(number_of_names):
    list_names = input()

    unique_names.add(list_names)



# for name in unique_names:
#
#     print(name)

print('\n'.join(unique_names))