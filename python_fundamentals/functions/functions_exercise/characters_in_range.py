def char_range(start_from, stop_at):
    result = []

    for chars in range(ord(start_from) +1, ord(stop_at)):
        result.append(chr(chars))

    return " ".join(result)

star_char = str(input())
stop_char = str(input())

print(char_range(star_char, stop_char))

# print(ord("b"))


