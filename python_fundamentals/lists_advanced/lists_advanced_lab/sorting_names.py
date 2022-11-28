some_names = input().split(", ")

sorted_names = sorted(some_names, key=lambda word: (-len(word), word))

print(sorted_names)