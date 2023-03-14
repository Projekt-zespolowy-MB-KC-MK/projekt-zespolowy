import populate_db
from library import Library


if __name__ == '__main__':
    library = Library('library.db')
    populate_db.create_test_data(library)
    all_books = library.get_all_books()
    all_borrowers = library.get_all_borrowers()
    all_borrows = library.get_all_borrowed_books()
