some_number = float(input())

if some_number == 0:
    print("zero")

elif some_number > 0:
    if some_number < 1:
        print('small positive')
    elif some_number > 1000000:
        print('large positive')
    else:
        print('positive')

else:
    if abs(some_number) < 1:
        print('small negative')
    elif abs(some_number) > 1000000:
        print('large negative')
    else:
        print('negative')
