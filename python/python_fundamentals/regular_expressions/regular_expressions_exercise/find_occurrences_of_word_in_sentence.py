import re

def finder(text, word):
    the_word = f"\\b{word}\\b"
    pattern = the_word

    the_finder = re.findall(pattern, text, flags=re.I)

    return len(the_finder)

some_text = input()
the_word = input()
print(finder(some_text, the_word))