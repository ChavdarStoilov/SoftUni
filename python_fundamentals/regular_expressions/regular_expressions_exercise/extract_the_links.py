import re


def get_links(links):

    pattern = r"(\www.)[a-zA-Z0-9\-]+[a-z.]*(\.[a-z]+)"

    regex = re.finditer(pattern, links)

    for link in regex:
        print(link.group())


some_text = input()

while some_text != "":

    get_links(some_text)

    some_text = input()
