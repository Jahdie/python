def my_func():
    summ = 0
    prev_summ = 0
    try:
        while True:
            print("Если хотите прервать ввод нажмите s")
            numbers = input("Введите строку чисел через пробел: ").split()
            """Проверяем введен ли символ s."""
            if numbers[-1] != 's':
                """Через цикл приводим элементы списка к типу int."""
                for i in range(len(numbers)):
                    numbers[i] = int(numbers[i])
                print(numbers)
                """Суммируем сумму эл-тов списка с предыдущей суммой эл-ов.
                   И выводим результат.
                """
                summ = sum(numbers) + prev_summ
                prev_summ = summ
                print(f"Сумма чисел: {summ}")
                continue
                """Если введен символ s, отрезаем от списка последний элемент,
                   и через цикл приводим эле-ты списка к типу int.
                """
            else:
                numbers = numbers[0:len(numbers) - 1]
                for i in range(len(numbers)):
                    numbers[i] = int(numbers[i])
                print(numbers)
                summ = sum(numbers) + prev_summ
                print(f"Сумма чисел: {summ}")
                break
                """В случае введения не цифры, а символа перехватываем ошибку,
                   сообщаем пользователю, вновь запускаем функцию.
                """
    except ValueError:
        print("\nВведены символы вместо цифр!!!\nПопробуйте снова!\n")
        my_func()


my_func()
