def read_next(*args):
    args = args

    for i in args:
        for n in i:
            yield n


for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')
