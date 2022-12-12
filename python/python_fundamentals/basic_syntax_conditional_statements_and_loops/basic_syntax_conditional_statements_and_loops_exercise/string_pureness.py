number_of_words = int(input())

list_characters = []


for words in range(number_of_words):
    word = str(input())

    for characters in range(len(word)):
        list_characters.append(word[characters])

    if "," in list_characters or "." in list_characters or "_" in list_characters:
        print(f"{word} is not pure!")
        list_characters.clear()
    else:
        print(f"{word} is pure.")
        list_characters.clear()
