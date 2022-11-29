class User:

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):

        if value == '':
            raise ValueError('Invalid username!')

        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):

        if value < 6:
            return ValueError('Users under the age of 6 are not allowed!')

        self.__age = value

    def __str__(self):
        pass
