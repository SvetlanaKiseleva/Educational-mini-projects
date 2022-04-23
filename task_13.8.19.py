t = int(input("Введите количество билетов: "))
tickets_price = 0

for i in range(t):
    user_age = int(input("Введите возраст посетителя: "))

    if user_age < 18:
        print("Проход на конференцию бесплатный.")
    elif 18 <= user_age < 25:
        tickets_price += 990
        print("Стоимость билета составит 990 рублей.")
    elif user_age >= 25:
        tickets_price += 1390
        print("Стоимость билета составит 1390 рублей.")

if t > 3:
    tickets_price = tickets_price * 0.9
    print("Сумма к оплате со скидкой 10% (от 4-х человек): ", tickets_price, "рублей")
else:
    print("Сумма к оплате: ", tickets_price, "рублей")