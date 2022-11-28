some_word = input().split(" ")
end_text = ""

for text in some_word:
    the_range = len(text)
    end_text += text * the_range

print(end_text)
