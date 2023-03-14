class Book:
    def __init__(self, book_id, isbn, genre, title, author, published):
        self.book_id = book_id
        self.isbn = isbn
        self.genre = genre
        self.title = title
        self.author = author
        self.published = published

    def print_info(self):
        print(f"Book ID: {self.book_id}")
        print(f"ISBN: {self.isbn}")
        print(f"Genre: {self.genre}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Published: {self.published}")
