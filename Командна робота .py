# Практична робота №3
# Завдання 2
# Командна робота
# Учасник команди
#
# Основа програми: Завдання 1, Варіант 3
#
# Нова функція учасника команди:
# редагування інформації про вже існуючу країну.


# Словник країн

countries = {
    "Ukraine": [603628, 37.0, "Europe"],
    "Poland": [312696, 37.5, "Europe"],
    "Germany": [357588, 84.4, "Europe"],
    "Japan": [377975, 123.3, "Asia"],
    "China": [9596961, 1409.0, "Asia"],
    "India": [3287263, 1428.0, "Asia"],
    "Egypt": [1002450, 112.7, "Africa"],
    "Kenya": [580367, 55.1, "Africa"],
    "Canada": [9984670, 40.1, "North America"],
    "Brazil": [8515767, 203.1, "South America"]
}


# Завдання для учасників команди
#
# 1. Реалізувати редагування інформації про країну.
# 2. Реалізувати пошук країни за назвою.
# 3. Реалізувати пошук країни з найбільшою площею.
# 4. Реалізувати пошук країни з найбільшим населенням.
# 5. Додати збереження словника у файл.
#
# Учасник команди обирає одну із запропонованих функцій
# та реалізує її у власній гілці Git.

# 1. Виведення всіх значень словника

def print_countries(countries):

    if len(countries) == 0:
        print("Словник порожній.")
        return

    print("\nСписок країн:")

    for country in countries:
        print(
            country,
            "- площа:", countries[country][0], "км²,",
            "населення:", countries[country][1], "млн,",
            "частина світу:", countries[country][2]
        )


# 2. Додавання нового запису

def add_country(countries):

    try:
        name = input("Введіть назву країни: ").strip()

        if name == "":
            raise ValueError("Назва країни не може бути порожньою.")

        if name in countries:
            print("Така країна вже є у словнику.")
            return

        area = float(input("Введіть площу країни (км²): "))
        population = float(input("Введіть населення (млн): "))
        continent = input("Введіть частину світу: ").strip()

        if area <= 0:
            raise ValueError("Площа повинна бути більшою за 0.")

        if population <= 0:
            raise ValueError("Населення повинно бути більшим за 0.")

        if continent == "":
            raise ValueError("Частина світу не може бути порожньою.")

        countries[name] = [area, population, continent]

        print("Країну", name, "додано.")

    except ValueError as error:
        print("Помилка:", error)


# 3. Видалення запису

def delete_country(countries):

    name = input(
        "Введіть назву країни для видалення: "
    ).strip()

    try:
        del countries[name]
        print("Країну", name, "видалено.")

    except KeyError:
        print(
            "Помилка! Країни",
            name,
            "немає у словнику."
        )

# 4. Виведення словника за відсортованими ключами

def print_sorted(countries):

    if len(countries) == 0:
        print("Словник порожній.")
        return

    print("\nКраїни в алфавітному порядку:")

    for country in sorted(countries.keys()):

        print(
            country,
            "- площа:", countries[country][0], "км²,",
            "населення:", countries[country][1], "млн,",
            "частина світу:", countries[country][2]
        )


# 5. Завдання варіанта
# Пошук країн Африки та Азії

def find_africa_asia(countries):

    found = False

    print("\nКраїни, розташовані в Африці або Азії:")

    for country in countries:

        continent = countries[country][2]

        if continent == "Africa" or continent == "Asia":

            print(country)
            found = True

    if not found:
        print("Таких країн у словнику немає.")



# 6. НОВА ФУНКЦІЯ УЧАСНИКА КОМАНДИ
# Редагування інформації про країну

def edit_country(countries):

    print("\n----- Редагування інформації про країну -----")

    name = input(
        "Введіть назву країни для редагування: "
    ).strip()

    # Перевірка наявності країни
    if name not in countries:

        print(
            "Помилка! Країни",
            name,
            "немає у словнику."
        )

        return

    # Виведення поточних даних
    print("\nПоточна інформація:")

    print(
        "Площа:",
        countries[name][0],
        "км²"
    )

    print(
        "Населення:",
        countries[name][1],
        "млн"
    )

    print(
        "Частина світу:",
        countries[name][2]
    )

    try:

        # Введення нових даних
        area = float(
            input("Введіть нову площу (км²): ")
        )

        population = float(
            input("Введіть нове населення (млн): ")
        )

        continent = input(
            "Введіть нову частину світу: "
        ).strip()

        # Перевірка даних
        if area <= 0:

            print(
                "Помилка! Площа повинна бути більшою за 0."
            )

            return

        if population <= 0:

            print(
                "Помилка! Населення повинно бути більшим за 0."
            )

            return

        if continent == "":

            print(
                "Помилка! Частина світу не може бути порожньою."
            )

            return

        # Зміна інформації
        countries[name] = [
            area,
            population,
            continent
        ]

        print(
            "\nІнформацію про країну",
            name,
            "успішно змінено."
        )

    except ValueError:

        print(
            "Помилка! Площа та населення "
            "повинні бути числами."
        )


# Головне меню

def menu():

    while True:

        print("\n======================================")
        print("        РОБОТА ЗІ СЛОВНИКОМ")
        print("======================================")

        print("1 - Вивести всі країни")
        print("2 - Додати країну")
        print("3 - Видалити країну")
        print("4 - Вивести країни за відсортованими ключами")
        print("5 - Знайти країни Африки та Азії")
        print("6 - Редагувати інформацію про країну")
        print("0 - Завершити програму")

        try:

            choice = int(
                input("\nОберіть пункт меню: ")
            )

            if choice == 1:

                print_countries(countries)

            elif choice == 2:

                add_country(countries)

            elif choice == 3:

                delete_country(countries)

            elif choice == 4:

                print_sorted(countries)

            elif choice == 5:

                find_africa_asia(countries)

            elif choice == 6:

                edit_country(countries)

            elif choice == 0:

                print("\nПрограму завершено.")
                break

            else:

                print(
                    "Помилка! Такого пункту меню немає."
                )

        except ValueError:

            print(
                "Помилка! Необхідно ввести число."
            )



# Запуск програми

menu()
