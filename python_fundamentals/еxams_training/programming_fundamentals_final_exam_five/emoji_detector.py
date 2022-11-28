import re

def emoji(text):
    threshold = 1
    all_emoji = []

    emoji_regex = r"(::[A-Z][a-z]{2,}::)|([*]+[A-Z][a-z]{2,}[*]+)|(\d)"

    regex = re.finditer(emoji_regex, text)

    for group in regex:
        finder = group.group()

        if finder.isdigit():
            threshold *= int(finder)
        else:
            all_emoji.append(finder)


    print(f"Cool threshold: {threshold}")
    print(f"{len(all_emoji)} emojis found in the text. The cool ones are:")
    cooler = 0
    for emo in all_emoji:
        for checker in emo:
            if checker.isalpha():
                cooler += ord(checker)
        if cooler > threshold:
            print(emo)

        cooler = 0


some_text = input()
emoji(some_text)