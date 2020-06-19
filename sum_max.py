def my_func(num_1, num_2, num_3):
    string = []
    string.append(num_1)
    string.append(num_2)
    string.append(num_3)
    string.pop(string.index(min(string)))
    return sum(string)


print(my_func(int(input("Введите 1-е число: ")), int(input("Введите 2-е число: ")), int(input("Введите 3-е число: "))))
