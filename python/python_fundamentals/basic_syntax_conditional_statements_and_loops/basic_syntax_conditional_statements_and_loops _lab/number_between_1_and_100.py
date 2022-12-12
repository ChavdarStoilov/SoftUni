some_number = float(input())

while some_number < 1 or some_number > 100:
    some_number = float(input())


print(f"The number {some_number} is between 1 and 100")