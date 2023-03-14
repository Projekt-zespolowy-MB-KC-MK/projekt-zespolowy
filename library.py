import sqlite3
from datetime import datetime, timedelta
import uuid
from borrower import Borrower
from book import Book
from borrow import Borrow


class Library:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

        # Create borrowers table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS borrowers (
                borrower_id INTEGER PRIMARY KEY,
                name TEXT,
                surname TEXT,
                phone_number TEXT,
                email TEXT
            )
        ''')

        # Create books table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                isbn TEXT,
                genre TEXT,
                title TEXT,
                author TEXT,
                published TEXT
            )
        ''')

        # Create borrowed_books table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS borrowed_books (
                borrow_id TEXT PRIMARY KEY,
                borrower_id INTEGER,
                book_id INTEGER,
                borrow_date DATE,
                borrow_time TIME,
                due_time DATE,
                FOREIGN KEY (borrower_id) REFERENCES borrowers (borrower_id),
                FOREIGN KEY (book_id) REFERENCES books (id)
            )
        ''')
    def add_borrower(self, borrower):
        self.cursor.execute('''
            INSERT INTO borrowers (name, surname, phone_number, email)
            VALUES (?, ?, ?, ?)
        ''', (borrower.name, borrower.surname, borrower.phone_number, borrower.email))

        self.conn.commit()

    def add_book(self, book):
        self.cursor.execute('''
            SELECT id FROM books WHERE id = ?
        ''', (book.book_id,))
        result = self.cursor.fetchone()
        if result is not None:
            # book with this id already exists, handle error
            # ...
            print("book already exists")
        else:
            self.cursor.execute('''
                INSERT INTO books (id, isbn, genre, title, author, published)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (book.book_id, book.isbn, book.genre, book.title, book.author, book.published))

            self.conn.commit()

    def borrower_returns_book(self, borrower, book):
        borrower.return_book(book)
        book.return_book()
        self.cursor.execute("DELETE FROM borrowed_books WHERE borrower_id = ? AND book_id = ?", (borrower.id, book.id))
        self.cursor.execute("UPDATE books SET is_available = 1 WHERE id = ?", (book.id,))
        self.conn.commit()

    def lend_book_to_borrower(self, book, borrower, days=7):
        self.cursor.execute("SELECT COUNT(*) FROM borrowed_books WHERE book_id = ?", (book.book_id,))
        count = self.cursor.fetchone()[0]

        if count > 0:
            print("The book is already borrowed")
            return None

        else:
            borrow_id = uuid.uuid4().hex
            borrow_date = datetime.now().date().strftime('%Y-%m-%d')
            borrow_time = datetime.now().time().strftime('%H:%M:%S')
            due_time = datetime.now().date() + timedelta(days=days)

            self.cursor.execute("""
                INSERT INTO borrowed_books (borrow_id, borrower_id, book_id, borrow_date, borrow_time, due_time)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (borrow_id, borrower.borrower_id, book.book_id, borrow_date, borrow_time, due_time))

            self.conn.commit()

            return Borrow(borrow_id, borrower.borrower_id, book.book_id, borrow_date, borrow_time, due_time)
