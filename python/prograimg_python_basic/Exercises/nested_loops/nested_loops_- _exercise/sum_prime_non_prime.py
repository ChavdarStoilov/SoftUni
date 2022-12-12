some_number = input()

sum_of_prime = 0
sum_of_non_prime = 0

while some_number != "stop":
    number = int(some_number)
    if number < 0:
        print("Number is negative.")
        some_number = input()
        continue


    count = 0
    for numbers in range(1, number + 1):
        if number % numbers == 0:
            count += 1


    if count == 2:
        sum_of_prime += number
    else:
        sum_of_non_prime += number


    some_number = input()

print(f"Sum of all prime numbers is: {sum_of_prime}\n"
      f"Sum of all non prime numbers is: {sum_of_non_prime}")