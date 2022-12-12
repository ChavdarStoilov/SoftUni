word = input()

list_word = []
wordd = ""

while word != "End":


    if word == "SoftUni":
        word = input()
        continue
    else:
        for char in range(len(word)):
            list_word.append(word[char])
            list_word.append(word[char])


        for the_word in list_word:
            wordd += the_word

    print(wordd)
    wordd = ""

    list_word.clear()
    word = input()