numbers_list = input().split(", ")
result = 1

for i in numbers_list:
    number = int(i)
    if number <= 5:
        result *= number

    elif number > 5:
        result /= number

print(int(result))
