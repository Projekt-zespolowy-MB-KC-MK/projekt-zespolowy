import sqlite3
from datetime import datetime, timedelta
import uuid
from borrower import Borrower
from book import Book
from borrow import Borrow
from administrator import Administrator


class Library:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

        # Create borrowers table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS borrowers (
                user_id INTEGER PRIMARY KEY,
                name TEXT,
                surname TEXT,
                phone_number TEXT,
                email TEXT
            )
        ''')

        # Create administratrs table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS admistrators (
                user_id INTEGER PRIMARY KEY,
                name TEXT,
                surname TEXT,
                phone_number TEXT,
                email TEXT,
                password TEXT
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
            INSERT INTO borrowers (user_id, name, surname, phone_number, email)
            VALUES (?, ?, ?, ?, ?)
        ''', (borrower.user_id, borrower.name, borrower.surname, borrower.phone_number, borrower.email))

        self.conn.commit()

    def add_administrator(self, administrator):
        self.cursor.execute('''
            INSERT INTO administrators (user_id, name, surname, phone_number, email, password)
            VALUES (?, ?, ?, ?, ?,?)
        ''', (administrator.user_id, administrator.surname, administrator.phone_number, administrator.email,
              administrator.password))

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
        self.cursor.execute("DELETE FROM borrowed_books WHERE user_id = ? AND book_id = ?", (borrower.id, book.id))
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
            """, (borrow_id, borrower.user_id, book.book_id, borrow_date, borrow_time, due_time))

            self.conn.commit()

            return Borrow(borrow_id, borrower.user_id, book.book_id, borrow_date, borrow_time, due_time)

    def get_all_borrowed_books(self, limit=None):
        query = '''
            SELECT *
            FROM borrowed_books

        '''
        if limit is not None:
            query += f' LIMIT {limit}'

        self.cursor.execute(query)
        results = self.cursor.fetchall()
        borrows = []
        for result in results:
            borrow_id = result[0]
            borrower_id = result[1]
            book_id = result[2]
            borrow_date = datetime.strptime(result[3], '%Y-%m-%d').date()
            borrow_time = datetime.strptime(result[4], '%H:%M:%S').time()
            due_time = datetime.strptime(result[5], '%Y-%m-%d').date()

            borrow = Borrow(borrow_id, borrower_id, book_id, borrow_date, borrow_time, due_time)
            borrow.print_info()
            borrows.append(borrow)

        return borrows

    def get_all_borrowers(self, limit=None):
        query = '''
            SELECT *
            FROM borrowers
        '''
        if limit is not None:
            query += f' LIMIT {limit}'

        self.cursor.execute(query)
        results = self.cursor.fetchall()
        borrowers = []
        for result in results:
            borrower = Borrower(result[0], result[1], result[2], result[3], result[4])
            borrower.print_info()
            borrowers.append(borrower)
        return borrowers

    def get_all_books(self, limit=None):
        query = '''
            SELECT *
            FROM books
        '''
        if limit is not None:
            query += f' LIMIT {limit}'

        self.cursor.execute(query)
        results = self.cursor.fetchall()
        books = []
        for result in results:
            book_id, isbn, genre, title, author, published = result
            book = Book(book_id, isbn, genre, title, author, published)
            book.print_info()
            books.append(book)
        return books

    def get_borrower_by_id(self, borrower_id):
        self.cursor.execute('SELECT * FROM borrowers WHERE borrower_id = ?', (borrower_id,))
        result = self.cursor.fetchone()
        if result is not None:
            borrower = Borrower(result[0], result[1], result[2], result[3], result[4])
            return borrower
        else:
            print("Borrower not found")
            return None

    def get_administrator_by_id(self, admin_id):
        self.cursor.execute('SELECT * FROM adminstrators WHERE user_id = ?', (admin_id,))
        result = self.cursor.fetchone()
        if result is not None:
            admin = Administrator(result[0], result[1], result[2], result[3], result[4], result[4])
            return admin
        else:
            print("Admin not found")
            return None

    def get_book_by_id(self, book_id):
        self.cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
        result = self.cursor.fetchone()
        if result is not None:
            book = Book(result[0], result[1], result[2], result[3], result[4], result[5])
            return book
        else:
            print("Book not found")
            return None
