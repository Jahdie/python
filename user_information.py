def user_info(name, surname, birth_year, city, email, tel_number):
    return print(f"{name}, {surname}, {birth_year}, {city}, {email}, {tel_number}")


user_info(name=input("Введите своё имя: "),
          surname=input("Введите свою фамилию: "),
          birth_year=input("Введите год своего рождениия: "),
          city=input("Введите город проживания: "),
          email=input("Введите адрес электронной почты: "),
          tel_number=input("Введите номер телефона: "))
