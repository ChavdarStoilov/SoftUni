def characters_long(passwd):
    if 6 <= len(passwd) <= 10:
        return True

    print("Password must be between 6 and 10 characters")
    return False

def special_char(passwd):
    if passwd.isalnum():
        return True

    print("Password must consist only of letters and digits")
    return False


def number_check(passwd):
    count_number = 0

    for number in passwd:
        if number.isdigit():
            count_number += 1
        if count_number >= 2:
            return True

    print("Password must have at least 2 digits")
    return False


some_password = str(input())

validator = characters_long(some_password), number_check(some_password), special_char(some_password)

if all(validator):
    print("Password is valid")

