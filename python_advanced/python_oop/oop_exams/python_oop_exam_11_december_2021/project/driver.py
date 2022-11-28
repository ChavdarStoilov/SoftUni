class Driver:

    def __init__(self, name, car = None, number_of_wins = 0):
        self.name = name
        self.car = car
        self.number_of_wins = number_of_wins
        
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):

        if value.isspace() or not value:
            raise ValueError("Name should contain at least one character!")

        self.__name = value