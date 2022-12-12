def palindrome(numbers):
    for number in numbers:
        first_num = int(number[0])
        last_num = int(number[-1])
        if first_num == last_num:
            print("True")
        else:
            print("False")



some_numer = input().split(", ")

palindrome(some_numer)
