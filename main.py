def currency_converter():
    print("Вітаємо у конвертері валют!")

    # Введення курсів валют
    usd_to_uah = float(input("Введіть курс долара (USD до UAH): "))
    eur_to_uah = float(input("Введіть курс євро (EUR до UAH): "))

    while True:
        print("\nОберіть дію:")
        print("1. Конвертувати UAH в USD")
        print("2. Конвертувати UAH в EUR")
        print("3. Конвертувати USD в UAH")
        print("4. Конвертувати EUR в UAH")
        print("5. Вийти")

        choice = input("Ваш вибір: ")

        if choice == '1':
            amount = float(input("Введіть суму в UAH: "))
            print(f"{amount} UAH = {amount / usd_to_uah:.2f} USD")
        elif choice == '2':
            amount = float(input("Введіть суму в UAH: "))
            print(f"{amount} UAH = {amount / eur_to_uah:.2f} EUR")
        elif choice == '3':
            amount = float(input("Введіть суму в USD: "))
            print(f"{amount} USD = {amount * usd_to_uah:.2f} UAH")
        elif choice == '4':
            amount = float(input("Введіть суму в EUR: "))
            print(f"{amount} EUR = {amount * eur_to_uah:.2f} UAH")
        elif choice == '5':
            print("Дякуємо за використання конвертера валют!")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


currency_converter()
