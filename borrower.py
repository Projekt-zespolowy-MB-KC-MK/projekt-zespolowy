class Borrower:
    def __init__(self, borrower_id, name, surname, phone_number, email):
        self.borrower_id = borrower_id
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.email = email

    def print_info(self):
        print(f"Borrower ID: {self.borrower_id}")
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Phone number: {self.phone_number}")
        print(f"Email: {self.email}")
