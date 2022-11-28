the_key = int(input())
lines = int(input())

the_word = ""

for chars in range(lines):
    letter = str(input())
    dec = ord(letter)
    the_word += chr(dec + the_key)

print(the_word)


