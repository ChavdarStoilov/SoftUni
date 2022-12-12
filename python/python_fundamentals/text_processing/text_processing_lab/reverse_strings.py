some_text = input()

while some_text != "end":
    word = some_text
    reversed_word = ""
    for text in range(len(word) -1, -1, -1):
        reversed_word += word[text]

    print(f"{word} = {reversed_word}")

    some_text = input()