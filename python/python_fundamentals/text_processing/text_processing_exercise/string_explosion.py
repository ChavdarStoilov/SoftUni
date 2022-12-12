some_string = input()

end_result = ""
strength = 0

for char_index in range(len(some_string)):
    if some_string[char_index] == ">":
        end_result += some_string[char_index]
    elif not some_string[char_index].isdigit():
        end_result += some_string[char_index]
    else:
        strength = int(some_string[char_index])

    if strength > 1 and some_string[char_index + 1] != ">":
        result = some_string.replace(some_string[char_index + strength], "")
        end_result = result


print(end_result)