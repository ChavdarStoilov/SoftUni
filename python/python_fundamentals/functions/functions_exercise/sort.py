def sort(numbers):
    sorted_numbers = []
    for number in numbers:
        sorted_numbers.append(int(number))

    return sorted(sorted_numbers)

numbers = input().split()

print(sort(numbers))