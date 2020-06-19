def power():
    try:
        x = int(input("Введите положительное число: "))
        while x <= 0: x = int(input("Введите положительное число: "))
        y = int(input("Введите отрицательную степень: "))
        while y >= 0: y = int(input("Введите отрицательную степень: "))
    except ValueError:
        print("\nВведены символы вместо цифр!!!\nПопробуйте снова!\n")
        power()
    else:
        list = []
        pow = 1
        """создаем список из x-элем-ов у-раз"""
        list = [x for _ in range(abs(y))]
        """берем элемент списка и перемножаем с нараcтанием pow, делим на 1"""
        for n in list: pow = pow * n
        pow = 1 / pow
        print(pow)
        return print(f"Степень {y} числа {x} равно {pow}")


power()
