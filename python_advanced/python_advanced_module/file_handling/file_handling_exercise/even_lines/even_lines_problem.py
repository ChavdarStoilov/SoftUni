def replace(word):
    symbols = ["-", ",", ".", "!", "?"]
    for symbol in symbols:
        if symbol in word:
            word = word.replace(symbol, '@')

    return word

def reverser(line_text):

    end_result = []

    line_text = line_text[::-1].split()

    for word in line_text:
        normal_word = word[::-1]
        end_result.append(replace(normal_word))

    return " ".join(end_result)

with open('text.txt', 'r') as even:
    lines = even.readlines()
    for line in range(len(lines)):
        if line % 2 == 0:
            print(reverser(lines[line]))

    even.close()

