def reverser(numbers):

    return " ".join([numbers.pop() for _ in range(len(numbers))])


some_numbers = input().split()

print(reverser(some_numbers))