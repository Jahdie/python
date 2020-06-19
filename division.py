def division(number_1, number_2):
    try:
        div = number_1 / number_2
    except ZeroDivisionError:
        print("Деление на ноль!")
    else:
        return div


print(division(int(input("Введите первое число: ")), int(input("Введите второе число: "))))
