first_word = str(input())
second_word = str(input())

end_string = first_word


for first in range(len(second_word)):
    left_side = second_word[:first + 1]
    right_side = first_word[first + 1:]
    current_string = left_side + right_side

    if current_string == end_string:
        continue

    print(current_string)
    end_string = current_string
