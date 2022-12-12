some_number = int(input())

synonym_dict = {}

for _ in range(some_number):
    word = input()
    the_synonym = input()

    if word not in synonym_dict:
        synonym_dict[word] = []
    synonym_dict[word].append(the_synonym)


for words in synonym_dict:
    print(f"{words} - {', '.join(synonym_dict[words])}")