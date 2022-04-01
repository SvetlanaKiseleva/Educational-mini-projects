t = int(input("Введите количество билетов: "))
tickets_price = 0
user_age = int(input("Введите ваш возраст: "))
for tickets_price in range(t, t + 1):
    if user_age < 18:
        print("Проход на конференцию бесплатный.")
    elif 18 <= user_age < 25:
        print("Стоимость одного билета составит 990 рублей.")
        if t > 3:
            tickets_price = t * 990 * 0.9
            print("Сумма к оплате со скидкой 10% (от 4-х человек): ", tickets_price, "рублей")
        else:
            tickets_price = t * 990
            print("Сумма к оплате: ", tickets_price, "рублей")
    elif user_age >= 25:
        print("Стоимость одного билета составит 1390 рублей.")
        if t > 3:
            tickets_price = t * 1390 * 0.9
            print("Сумма к оплате со скидкой 10% (от 4-х человек): ", tickets_price, "рублей")
        else:
            tickets_price = t * 1390
            print("Сумма к оплате: ", tickets_price, "рублей")