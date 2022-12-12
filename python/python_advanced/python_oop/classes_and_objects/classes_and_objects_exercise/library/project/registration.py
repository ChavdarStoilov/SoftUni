class Registration:

    def add_user(self, user, library):

        if user not in library.user_records:
            library.user_records.append(user)

        return f'User with id = {user.user_id} already registered in the library!'

    def remove_user(self, user, library):

        if user in library.user_records:
            library.user_records.remove(user)

        return 'We could not find such user to remove!'

    def change_username(self, user_id: int, new_username: str, library):

        for users in library.user_records:
            if users.user_id == user_id:
                if users.username != new_username:
                    if users.username in library.rented_books:
                        rented_books = library.rented_books[users.username]
                        library.rented_books.pop(users.username)
                        library.rented_books[new_username] = rented_books
                    users.username = new_username

                    return f'Username successfully changed to: {new_username} for user id: {user_id}'

                return 'Please check again the provided username - it should be different than the username used so far!'

        return f'There is no user with id = {user_id}!'
