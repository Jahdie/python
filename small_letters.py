def int_func(word):
    word_format = ""
    """Функция принимает word строку и переберает какждый ёё элемент.
        Если символ является строчной латинской буквой, то с помощью конкатенации
        формирует новую строку word_format c заглавной буквы, и функция её же и возвращает.
    """
    for char in word:
        if ord(char) >= 97 and ord(char) <= 122:
            word_format = word_format + char
    word_format = word_format.title()
    return word_format


# Вводим слова через прробел, формируем список, перебираем с помощью функции.
# Формируем новый список, приводим его к строке.
print(int_func(input("Введите слово: ")))
words_format = []
words = input("Введите слова через пробел: ").split()
for word in words:
    words_format.append(int_func(word))
print(' '.join(words_format))
