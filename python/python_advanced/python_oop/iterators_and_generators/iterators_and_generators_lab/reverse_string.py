def reverse_text(text):
    text_chars = [char for char in text]

    while text_chars:
        yield text_chars.pop()


for char in reverse_text("step"):
    print(char, end='')
