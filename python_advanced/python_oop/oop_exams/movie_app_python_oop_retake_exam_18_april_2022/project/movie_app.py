from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):

        for user in self.users_collection:
            if user.username == username:
                raise Exception('User already exists!')

        user = User(username, age)
        self.users_collection.append(user)
        return f'{username} registered successfully.'

    def upload_movie(self, username: str, movie):

        if movie in self.movies_collection:
            raise Exception('Movie already added to the collection!')

        for user in self.users_collection:
            if user.username == username:
                    if movie.owner == user:
                        self.movies_collection.append(movie)
                        user.movies_owned.append(movie)
                        return f'{username} successfully added {movie.title} movie.'
                    else:
                        raise Exception(f'{username} is not the owner of the movie {movie.title}!')

        raise Exception('This user does not exist!')

    def edit_movie(self, username: str, movie, **kwargs):

        if movie not in self.movies_collection:
            raise Exception(f'The movie {movie.title} is not uploaded!')


        for user in self.users_collection:
            if user.username == username:
                if movie.owner == user:
                    for key, value in kwargs.items():
                        if key == 'title':
                            movie.title = value
                        elif key == 'year':
                            movie.year = value
                        elif key == 'age_restriction':
                            movie.age_restriction = value

                    return f'{username} successfully edited {movie.title} movie.'
                else:
                    raise Exception(f'{username} is not the owner of the movie {movie.title}!')


    def delete_movie(self, username: str, movie):

        if movie not in self.movies_collection:
            raise Exception(f'The movie {movie.title} is not uploaded!')

        for user in self.users_collection:
            if user.username == username:
                if movie.owner == user:
                    self.movies_collection.remove(movie)
                    user.movies_owned.remove(movie)
                    return f'{username} successfully deleted {movie.title} movie.'
                else:
                    raise Exception(f'{username} is not the owner of the movie {movie.title}!')


    def like_movie(self, username: str, movie):

        for user in self.users_collection:
            if user.username == username:
                if movie in user.movies_liked:
                    raise Exception(f'{username} already liked the movie {movie.title}!')

                elif movie in user.movies_owned:
                    raise Exception(f'{username} is the owner of the movie {movie.title}!')

                else:
                    movie.likes += 1
                    user.movies_liked.append(movie)
                    return f'{username} liked {movie.title} movie.'

    def dislike_movie(self, username: str, movie):
        pass

    def display_movies(self):
        pass

    def __str__(self):
        pass
