from user import User

class Borrower(User):
    def __init__(self, user_id, name, surname, phone_number, email):
        super().__init__(user_id, name, surname, phone_number, email)
