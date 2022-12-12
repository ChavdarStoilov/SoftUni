some_word_keys = input().split(", ")
some_text = input()

for word in some_word_keys:
    while word in some_text:
        some_text = some_text.replace(word, "*" * len(word))


print(some_text)