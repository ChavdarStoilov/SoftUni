from collections import deque


def seat_checker(seats, chars, first_numbers, second_numbers, used):
    char = chr(chars)
    first_combination = str(first_numbers[0]) + char
    not_match = False

    second_combination = str(second_numbers[-1]) + char
    if first_combination not in used and second_combination not in used:
        if first_combination in seats:
            first_numbers.popleft()
            second_numbers.pop()
            return first_combination, first_numbers, second_numbers
        elif second_combination in seats:
            first_numbers.popleft()
            second_numbers.pop()
            return second_combination, first_numbers, second_numbers
        else:
            first_numbers.append(first_numbers.popleft())
            second_numbers.insert(0, second_numbers.pop())
            not_match = True
            return not_match, first_numbers, second_numbers
    else:
        first_numbers.popleft()
        second_numbers.pop()
        not_match = True
        return not_match, first_numbers, second_numbers


seats = input().split(', ')
numbers_one = deque(int(x) for x in input().split(', '))
numbers_two = [int(x) for x in input().split(', ')]

used_seats = []
rotations = 0

while len(used_seats) < 3 and rotations < 10:
    char = numbers_one[0] + numbers_two[-1]

    used_seat, numbers_one, numbers_two = seat_checker(seats, char, numbers_one, numbers_two, used_seats)

    if used_seat in seats:
        used_seats.append(used_seat)
    rotations += 1


print(f'Seat matches: {", ".join(used_seats)}')
print(f'Rotations count: {rotations}')
