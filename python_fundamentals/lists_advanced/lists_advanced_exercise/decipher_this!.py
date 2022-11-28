def decipher(secret_message):
    final_message = []

    for message in secret_message:
        code = ""
        for digits in message:
            if digits.isdigit():
                code += digits

        final_message.append(chr(int(code)))
        


some_secret_message = input().split()
decipher(some_secret_message)
