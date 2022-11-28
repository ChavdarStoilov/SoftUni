def ascii_func(the_chars):
    ascii_dict = {}

    for char in the_chars:
        ascii_dict[char] = int(ord(char))

    return ascii_dict



char = input().split(", ")
print(ascii_func(char))