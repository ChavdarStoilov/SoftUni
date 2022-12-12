some_text = input()

digits = ""
letters = ""
other = ""


for chars in some_text:
    if chars.isdigit():
        digits += chars
    elif chars.isalpha():
        letters += chars
    else:
        other += chars

print(digits)
print(letters)
print(other)