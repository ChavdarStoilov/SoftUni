some_word = input()
vowels = ["a", "o", "u", "e", "i"]

result = [char for char in some_word if char.lower() not in vowels]

print("".join(result))