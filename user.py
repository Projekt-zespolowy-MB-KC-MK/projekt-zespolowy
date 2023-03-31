class User:
    def __init__(self, user_id, name, surname, phone_number, email):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.email = email

    def print_info(self):
        print(f"User ID: {self.user_id}")
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Phone number: {self.phone_number}")
        print(f"Email: {self.email}")
