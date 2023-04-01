from user import User

class Borrower(User):
    def __init__(self, borrower_id, name, surname, phone_number, email):
        super().__init__(borrower_id, name, surname, phone_number, email)
