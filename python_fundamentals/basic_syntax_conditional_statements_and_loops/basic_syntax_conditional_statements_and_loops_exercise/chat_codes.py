number = int(input())

for message in range(number):
    second_numer = int(input())

    if second_numer == 88:
        print("Hello")
    elif second_numer == 86:
        print("How are you?")
    elif 88 > second_numer:
        print("GREAT!")
    elif second_numer > 88:
        print("Bye.")
