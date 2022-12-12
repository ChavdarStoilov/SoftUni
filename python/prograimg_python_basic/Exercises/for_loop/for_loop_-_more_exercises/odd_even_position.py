import sys

some_number_for_n = int(input())

odd_max_number = -sys. maxsize
odd_min_number = sys.maxsize
even_max_number = -sys. maxsize
even_min_number = sys.maxsize
odd_sum = 0
even_sum = 0

for numbers in range(1, some_number_for_n + 1):
    number = float(input())

    if numbers % 2 == 0:
        even_sum += number
        if even_max_number < number:
            even_max_number = number
        if even_min_number > number:
            even_min_number = number
    else:
        odd_sum += number
        if odd_max_number < number:
            odd_max_number = number
        if odd_min_number > number:
            odd_min_number = number


print(f"OddSum={odd_sum:.2f},")

if odd_min_number == sys.maxsize:
    print("OddMin=No,")
else:
    print(f"OddMin={odd_min_number:.2f},")
if odd_max_number == - sys. maxsize:
    print("OddMax=No,")
else:
    print(f"OddMax={odd_max_number:.2f},")

print(f"EvenSum={even_sum:.2f},")

if even_min_number == sys.maxsize:
    print("EvenMin=No,")
else:
    print(f"EvenMin={even_min_number:.2f},")

if even_max_number == - sys. maxsize:
    print("EvenMax=No")
else:
    print(f"EvenMax={even_max_number:.2f}")
