import re

def dates_matches(text):

    pattern = r"\b(?P<day>\d{2})([\/.-])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b"

    groups = re.finditer(pattern, text)

    for date in groups:
        days = date.group("day")
        months = date.group("month")
        years = date.group("year")

        print(f"Day: {days}, Month: {months}, Year: {years}")



some_dates = input()
dates_matches(some_dates)