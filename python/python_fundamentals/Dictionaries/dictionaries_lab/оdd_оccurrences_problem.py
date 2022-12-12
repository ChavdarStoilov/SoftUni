some_words = input().split()

counter = {}

for word in some_words:
    lower_word = word.lower()
    if lower_word not in counter.keys():
        counter[lower_word] = 1
    else:
        counter[lower_word] += 1



end_result = [end_word for end_word, value in counter.items() if value % 2 != 0]
print(" ".join(end_result))