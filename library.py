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
