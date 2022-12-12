def get_primes(some_number_list):

    for number in some_number_list:
        if number > 1:
            for num in range(2, number):
                if number % num == 0:
                    break
            else:
                yield number

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))