class Player:
    used_names = set()
    MAX_STAMINA = 100
    MIN_STAMINA = 0

    def __init__(self, name: str, age: int, stamina = 100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        self.used_names.add(self.__name)
        return self.__name

    @name.setter
    def name(self, value):

        if value == '':
            raise ValueError('Name not valid!')

        if value in self.used_names:
            raise Exception(f'Name {value} is already used!')

        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):

        if value < 12:
            raise ValueError('The player cannot be under 12 years old!')

        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):

        if self.MAX_STAMINA < value or value < self.MIN_STAMINA:
            raise ValueError('Stamina not valid!')

        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.stamina < self.MAX_STAMINA

    def __str__(self):
        return f'Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}'
