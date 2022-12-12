counter_char = {}

some_string = input().split()

for word in some_string:
    for char in word:
        if char not in counter_char:
            counter_char[char] = 1
        else:
            counter_char[char] += 1


for chars, count in counter_char.items():
    print(f"{chars} -> {count}")