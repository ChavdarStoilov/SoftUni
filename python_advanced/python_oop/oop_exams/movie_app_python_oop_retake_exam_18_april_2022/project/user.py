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

        if not value:
            raise ValueError('Invalid username!')

        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):

        if value < 6:
            raise ValueError('Users under the age of 6 are not allowed!')

        self.__age = value

    def __str__(self):
        movies_liked = [f'{movies.details()}\n' for movies in self.movies_liked]
        movies_owner = [f'{movies.details()}\n' for movies in self.movies_owned]

        result_liked = "\n".join(movies_liked) if movies_liked else 'No movies liked.'
        result_owner = "\n".join(movies_owner) if movies_owner else 'No movies owned.'


        return f'Username: {self.username}, Age: {self.age}\n' \
               f'Liked movies:\n' \
               f'{result_liked.strip()}\n' \
               f'Owned movies:\n' \
               f'{result_owner.strip()}'
