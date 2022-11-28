some_number = int(input())


for numbers in range(2, some_number + 1):
    if some_number % numbers == 0:
        print("False")
        break
    else:
        print("True")
        break