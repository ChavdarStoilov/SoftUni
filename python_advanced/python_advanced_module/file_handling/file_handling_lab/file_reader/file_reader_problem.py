def sum_numbers(*args: str):

    result = 0

    for tuple_result in args:
        for the_number in tuple_result:
            result += int(the_number)

    return result

with open('numbers.txt', 'r') as number:

    print(sum_numbers(tuple(num.replace('\n', "") for num in number.readlines())))