class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            return f'The book {book.title} with author {book.author} was add in library'
        return f'The book {book.title} already in library'

    def find_book(self, title):

        for book in self.books:
            if book.title == title:
                return title

        return f'The book {title} not in library'