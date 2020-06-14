lst = input("Введите список: ").split()
for id, item in enumerate(lst, 1):
    print(f"{id} - {item[:10]}")
