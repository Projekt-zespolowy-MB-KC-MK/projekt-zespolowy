import populate_db
from library import Library


if __name__ == '__main__':
    library = Library('library.db')
    populate_db.create_test_data(library)
    all_books = library.get_all_books()
    all_borrowers = library.get_all_borrowers()
    all_borrows = library.get_all_borrowed_books()
    print("list borrowed books by 12345678901 id")
    all_borrowed_by_this_id = library.get_all_users_borrowed_books(12345678901)
    print("list borrowed books by 9876543210 id")
    all_borrowed_by_this_id = library.get_all_users_borrowed_books(9876543210)
