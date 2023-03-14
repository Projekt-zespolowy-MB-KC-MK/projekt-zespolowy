from borrower import Borrower
from book import Book


# utworzona do celów testowych, zaludnia tablice aby można było przeprowadzić testowanie
def create_test_data(library):
    # Tworzenie 2 wypożyczających
    borrower1 = Borrower('12345678901', 'Jan', 'Kowalski', '123456789', 'jan.kowalski@example.com')
    borrower2 = Borrower('09876543210', 'Anna', 'Nowak', '987654321', 'anna.nowak@example.com')

    # Tworzenie 10 książek
    book1 = Book('1234', '9788374954544', 'Science fiction', 'Dune', 'Frank Herbert', '1965')
    book2 = Book('5678', '9780061059002', 'Fantasy', 'A Game of Thrones', 'George R.R. Martin', '1996')
    book3 = Book('9012', '9783453319171', 'Thriller', 'The Da Vinci Code', 'Dan Brown', '2003')
    book4 = Book('3456', '9781501161610', 'Autobiography', 'Born a Crime', 'Trevor Noah', '2016')
    book5 = Book('7890', '9780345803481', 'Classic', '1984', 'George Orwell', '1949')
    book6 = Book('2345', '9780140283334', 'Literary Fiction', 'To Kill a Mockingbird', 'Harper Lee', '1960')
    book7 = Book('6789', '9780006479888', 'Romance', 'Bridget Jones\'s Diary', 'Helen Fielding', '1996')
    book8 = Book('1235', '9780525478812', 'Mystery', 'The Girl with the Dragon Tattoo', 'Stieg Larsson', '2005')
    book9 = Book('5679', '9780141187761', 'Drama', 'A Streetcar Named Desire', 'Tennessee Williams', '1947')
    book10 = Book('9013', '9781501164574', 'Humor', 'Bossypants', 'Tina Fey', '2011')

    #dodanie wypożyczających oraz książek do bazy danych
    library.add_borrower(borrower1)
    library.add_borrower(borrower2)
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)
    library.add_book(book6)
    library.add_book(book7)
    library.add_book(book8)
    library.add_book(book9)
    library.add_book(book10)

    # Wypożyczanie książek
    borrow1_book1 = library.lend_book_to_borrower(book1, borrower1)
    borrow1_book2 = library.lend_book_to_borrower(book2, borrower1)
    borrow2_book1 = library.lend_book_to_borrower(book3, borrower2)

    # Wyświetlenie informacji o wypożyczeniach
    #print(f'Borrower 1 borrowed {borrow1_book1.book.title} and {borrow1_book2.book.title}')
    #print(f'Borrower 2 borrowed {borrow2_book1.book.title}')
