number_of_lines = int(input())

longest_intersection = []

for _ in range(number_of_lines):

    first_start, second_start = input().split('-')

    first_start_range, first_end_range = map(int, first_start.split(','))
    second_start_range, second_end_range = map(int, second_start.split(','))

    first_set = {num for num in range(first_start_range, first_end_range + 1)}
    second_set = {num for num in range(second_start_range, second_end_range + 1)}

    intersection = first_set.intersection(second_set)

    if len(longest_intersection) < len(intersection):
        longest_intersection = intersection


end_result = [number for number in longest_intersection]
print(f'Longest intersection is {end_result} with length {len(longest_intersection)}')