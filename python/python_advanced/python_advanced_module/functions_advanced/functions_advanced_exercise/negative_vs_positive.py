def duel(*args):

    positive = 0
    negative = 0

    for str_number in args:
        int_number = int(str_number)

        if int_number > 0:
            positive += int_number
        else:
            negative += int_number



    print(f'{negative}\n'
          f'{positive}')

    if positive < abs(negative):
        return 'The negatives are stronger than the positives'
    else:
        return 'The positives are stronger than the negatives'

some_numbers = input().split()
print(duel(*some_numbers))