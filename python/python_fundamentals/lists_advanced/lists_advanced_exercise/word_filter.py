some_text = input().split()

even_words = [even for even in some_text if len(even) % 2 == 0]

print("\n".join(even_words))