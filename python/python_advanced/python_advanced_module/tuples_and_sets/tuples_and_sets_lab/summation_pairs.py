list_of_numbers = input().split()
target = int(input())

number_of_iterations = 0

unique_pairs = set()

while list_of_numbers:

    number = list_of_numbers.pop(0)

    for nums in list_of_numbers:
        number_of_iterations += 1

        if int(nums) + int(number) == target:
            print(f"{number} + {nums} = {target}")
            unique_pairs.add((int(number), int(nums)))

print(f'Iterations done: {number_of_iterations}')

for i in unique_pairs:
    print(i)