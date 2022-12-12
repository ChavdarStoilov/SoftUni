counter_word = {}
with open('text.txt', 'r') as reader:
    with open('words.txt', 'r') as list_words:
        words = list_words.read()
        sentences = reader.read().split()
        print(sentences)
        for word in words.split():
            counter_word[word] = sentences.count(word)

print(counter_word)
