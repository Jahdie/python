elements = input("Введиете пследовательность элементов через пробел: ").split()
for i in  range(0, len(elements)-1, 2):
    elements[i], elements[i + 1] = elements[i + 1], elements[i]
print(elements)
