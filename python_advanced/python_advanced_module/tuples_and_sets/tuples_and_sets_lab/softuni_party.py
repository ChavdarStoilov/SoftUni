
number_of_guests = int(input())

coming_persons = set()
missing_guests = set()

for _ in range(number_of_guests):
    coming_persons.add(input())

coming_guest = input()

while coming_guest != 'END':

    missing_guests.add(coming_guest)

    coming_guest = input()


missing_persons = list(coming_persons.difference(missing_guests))
print(len(missing_persons))

for person in sorted(missing_persons):

    print(person)