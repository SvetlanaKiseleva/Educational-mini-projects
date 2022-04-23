class Volunteers:
    def __init__(self, name, surname, sity, status):
        self.name = name
        self.surname = surname
        self.sity = sity
        self.status = status

    def print_info(self):
        return self.name, self.surname, self.sity, self.status

