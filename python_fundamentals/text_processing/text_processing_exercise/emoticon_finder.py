some_text = input()

for index in range(len(some_text)):
    if some_text[index] == ":":
        emoji = some_text[index:index+2]
        print(emoji)