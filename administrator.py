from user import User


class Administrator(User):
    def __init__(self, admin_id, name, surname, phone_number, email, password):
        super().__init__(admin_id, name, surname, phone_number, email)
        self.password = password

    def print_info(self):
        super().print_info()
