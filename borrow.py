class Borrow:
    def __init__(self, borrow_id, borrower_id, book_id, borrow_date, borrow_time, due_time):
        self.borrow_id = borrow_id
        self.borrower_id = borrower_id
        self.book_id = book_id
        self.borrow_date = borrow_date
        self.borrow_time = borrow_time
        self.due_time = due_time

    def print_info(self):
        print("Borrow ID:", self.borrow_id, "Borrower ID:", self.borrower_id, "Book ID:", self.book_id, "Borrow date:", self.borrow_date, "Borrow time:", self.borrow_time, "Due time:", self.due_time)
        #print("Borrower ID:", self.borrower_id)
        #print("Book ID:", self.book_id)
        #print("Borrow date:", self.borrow_date)
        #print("Borrow time:", self.borrow_time)
        #print("Due time:", self.due_time)
