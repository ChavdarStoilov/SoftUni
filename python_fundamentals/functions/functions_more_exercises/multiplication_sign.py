def negative_or_positive(first, second, third):
    if first == 0 or second == 0 or third == 0:
        return "zero"
    elif first < 0 or second < 0 or third < 0:
        if first < 0 and second > 0 and third > 0 or first > 0 and second < 0 and third > 0 or first > 0 and second > 0 and third < 0:
            return "negative"
        elif first < 0 and second < 0 and third < 0:
            return "negative"
        return "positive"
    elif first > 0 and second > 0 and third > 0:
        return "positive"



first_number = int(input())
second_number = int(input())
third_number = int(input())

print(negative_or_positive(first_number, second_number, third_number))