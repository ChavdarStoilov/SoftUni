class Library:

    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}


    def get_book(self, author: str, book_name: str, days_to_return: int, user):

        if author in self.books_available and book_name in self.books_available[author]:
                user.books.append(book_name)
                self.books_available[author].remove(book_name)

                if user.username not in self.rented_books:
                    self.rented_books[user.username] = {}

                self.rented_books[user.username][book_name] = days_to_return

                return f'{book_name} successfully rented for the next {days_to_return} days!'

        for rented in self.rented_books.values():
            for book, times in rented.items():
                if book == book_name:
                    return f'The book "{book_name}" is already rented and will be available in {times} days!'

    def return_book(self, author: str, book_name: str, user):

        if book_name in user.books:
                self.books_available[author].append(book_name)
                self.rented_books[user.username].pop(book_name)
                user.books.remove(book_name)

        return f'{user.username} doesn\'t have this book in his/her records!'
