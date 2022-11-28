some_text = str(input())

sum = 0
for text in some_text:
    if text == "a":
        sum += 1
    elif text == "e":
        sum += 2
    elif text == "i":
        sum += 3
    elif text == "o":
        sum += 4
    elif text == "u":
        sum += 5

print(sum)
