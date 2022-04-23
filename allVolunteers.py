from volunteers import Volunteers

person_1 = Volunteers("Иван", "Петров", "г.Москва", "статус 'Наставник'")
person_2 = Volunteers("Игорь", "Иванов", "г.Санкт-Петербург", "статус 'Волонтер'")
person_3 = Volunteers("Петр", "Кузнецов", "г.Самара", "статус 'Волонтер'")
person_4 = Volunteers("Мария", "Андреева", "г.Москва", "статус 'Наставник'")

print(person_1.print_info())
print(person_2.print_info())
print(person_3.print_info())
print(person_4.print_info())
