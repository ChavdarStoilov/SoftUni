some_words = input().split(", ")

end_result = ""

for word in some_words:
    if 3 <= len(word) <= 16 and word.isidentifier():
        print(word)
    elif 3 <= len(word) <= 16 and "_" in word or "-" in word:
        print(word)