import re


def email_validator(email):

    pattern = r"\b(?<=\s)([a-zA-Z0-9]+[._-]?)[a-zA-Z0-9]+@[a-z]+?[.-][a-z.]+\b"

    regex = re.finditer(pattern, email)

    for i in regex:
        print(i.group())



text_with_mails = input()
email_validator(text_with_mails)