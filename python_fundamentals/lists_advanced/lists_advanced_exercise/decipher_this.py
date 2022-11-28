def decipher_func(strings):
    final_result = []

    for word in strings:
        number = ""
        current_word = ""
        for letters in word:
            if letters.isdigit():
                number += letters
            else:
                break

        word = word.replace(number, "")
        current_word += chr(int(number))
        if len(word) >= 2:
            word = word[-1] + word[1:-1] + word[0]
        current_word += word
        final_result.append(current_word)

    return " ".join(final_result)

some_strings = input().split()

print(decipher_func(some_strings))