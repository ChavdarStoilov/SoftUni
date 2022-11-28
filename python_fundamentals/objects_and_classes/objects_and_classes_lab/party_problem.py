class Party:

    def __init__(self):
        self.all_guest = []

    def people(self):
        return ', '.join(self.all_guest)

    def total_guest(self):
        return len(self.all_guest)


party = Party()

names = input()
while names != "End":
    party.all_guest.append(names)
    names = input()

print(f"Going: {party.people()}")
print(f"Total: {party.total_guest()}")