def perfect_number(the_number):

    result = 0

    for number in range(1, the_number +1):
        test = the_number // number
        if the_number * number == the_number:
            result += number
        elif the_number == test * number:
            result += number

    if result // 2 == the_number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())

print(perfect_number(number))