import re



def checker(string):
    pattern = r'(?P<start>[#|$|*|&|%])([a-zA-Z]+)(?P=start)=(\d+)!!(.+)'

    result = re.finditer(pattern, string)

    for i in result:
        find = i.groups()

        name = find[1]
        number = int(find[2])
        geo_hash_code = find[3]

        if number == len(geo_hash_code):
            return f'Coordinates found! {name} -> {"".join([chr(ord(x) + number) for x in geo_hash_code])}'

    return None



while True:
    some_string = input()
    result = checker(some_string)

    if result is not None:
        print(result)
        break

    print("Nothing found!")
