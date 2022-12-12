import re

def finder(text):

    pattern = r"\b_[a-zA-Z1-9]+\b"

    the_finder = re.findall(pattern, text)

    return ",".join(the_finder).replace("_", "")


some_text = input()
print(finder(some_text))