import re


def mapper(maps):

    destination = []
    total_point = 0

    pattern = r"\b(?<=\=)[A-Z][a-zA-Z]{2,}(?=\=)|(?<=\/)[A-Z][a-zA-Z]{2,}(?=\/)\b"

    regex = re.finditer(pattern, maps)

    for the_maps in regex:
        destination.append(the_maps.group())
        total_point += len(the_maps.group())

    return f"Destinations: {', '.join(destination)}\n" \
           f"Travel Points: {total_point}"

the_maps = input()
print(mapper(the_maps))