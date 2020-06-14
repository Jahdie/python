products_analys = {
    "название": [],
    "цена": [],
    "количество": [],
    "ед": []
}
products = []
stop_enter = ""
i = 1
while stop_enter != "y":
    product = {
    "название": "",
    "цена": "",
    "количество": "",
    "ед": ""
     }
    product["название"] = input("Введите название: ")
    while product["название"] == "":
        product["название"] = input("Введите название: ")
    product["цена"] = input("Введите цену: ")
    while product["цена"].isdigit() == False:
        product["цена"] = input("Введите цену: ")
    product["количество"] = input("Введите количество: ")
    while product["количество"].isdigit() == False:
        product["количество"] = input("Введите количество: ")
    product["ед"] = input("Введите единицы измерения: ")
    while product["ед"] == "":
        product["ед"] = input("Введите единицы измерения: ")
    products.append((i, product))
    stop_enter = input("Введите 'y' если хотите прекратить ввод: ")
    i += 1
for p in products:
    n = 1
    products_analys["название"].append(p[n]["название"])
    products_analys["цена"].append(p[n]["цена"])
    products_analys["количество"].append(p[n]["количество"])
    products_analys["ед"].append(p[n]["ед"])
    n+=1
print(f"\nНазвание: {', '.join(products_analys['название'])}\nЦена: {', '.join(products_analys['цена'])}"
      f"\nКоличество: {', '.join(products_analys['количество'])}\nЕдиницы: {', '.join(products_analys['ед'])}")