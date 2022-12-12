import re
from errors import *

domains = ['.com', '.bg', '.org', '.net']

while True:

    email = input()

    if email == 'End':
        break

    pattern = '((\w+)@?\w+)(.\w+)'

    checker = re.findall(pattern, email)
    symbol_check, user_check, domain_check = checker[0][0], checker[0][1], checker[0][2]

    if len(user_check) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')
    elif '@' not in symbol_check:
        raise MustContainAtSymbolError('Email must contain @')
    elif domain_check not in domains:
        raise InvalidDomainError(f'Domain must be one of the following: {", ".join(domains)}')
    else:
        print('Email is valid')
