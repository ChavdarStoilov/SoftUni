year = int(input())
happy_year = False

while not happy_year:
    year += 1
    set_of_years = set()

    for i in range(len(str(year))):
        set_of_years.add(str(year)[i])

    happy_year =len(set_of_years) == len(str(year))

print(year)
