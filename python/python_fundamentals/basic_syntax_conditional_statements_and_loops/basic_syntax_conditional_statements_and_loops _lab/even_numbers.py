num_of_number = int(input())

for i in range(num_of_number):
    some_number = int(input())

    if some_number % 2 != 0:
        print(f"{some_number} is odd!")
        break

else:
    print("All numbers are even.")