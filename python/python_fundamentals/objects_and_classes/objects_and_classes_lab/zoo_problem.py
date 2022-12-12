class Zoo:
    __animals = 0

    def __init__(self, name_of_zoo):
        self.name_of_zoo = name_of_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):
        self.species = species
        self.name = name

        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        self.species = species
        if species == "mammal":
            return f"Mammals in {self.name_of_zoo}: {', '.join(self.mammals)}\nTotal animals: {self.__animals}"
        elif species == "fish":
            return f"Fishes in {self.name_of_zoo}: {', '.join(self.fishes)}\nTotal animals: {self.__animals}"
        elif species == "bird":
            return f"Birds in {self.name_of_zoo}: {', '.join(self.birds)}\nTotal animals: {self.__animals}"


name_of_the_zoo = input()
number_of_animals = int(input())
the_zoo = Zoo(name_of_the_zoo)
for _ in range(number_of_animals):
    animal = input().split()
    species = animal[0]
    the_name = animal[1]
    the_zoo.add_animals(species, the_name)

the_species = input()
print(the_zoo.get_info(the_species))