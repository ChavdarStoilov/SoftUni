some_word = str(input()).lower()

counter = 0
list_of_words = ["sand", "water", "fish", "sun"]
found_words = 0

for words in list_of_words:
    if words in some_word:
        word_count_txt = some_word.count(words)
        found_words += word_count_txt


print(found_words)