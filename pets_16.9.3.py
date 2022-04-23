class Transactions:
    def __init__(self, name, surname, cash):
        self.name = name
        self.surname = surname
        self.cash = cash

    def clients_info(self):
        return f"Клиент: {self.name} {self.surname}, Баланс: {self.cash}"

person_1 = Transactions("Иван", "Петров", 50)
print(person_1.clients_info())
