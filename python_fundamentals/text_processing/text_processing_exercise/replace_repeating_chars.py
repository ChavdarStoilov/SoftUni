some_string = input()

end_result = ""

for char in range(len(some_string)):
    if char == len(some_string) - 1:
        end_result += some_string[char]
        break

    current_char = some_string[char]
    next_char = some_string[char + 1]

    if current_char != next_char:
        end_result += current_char

print(end_result)