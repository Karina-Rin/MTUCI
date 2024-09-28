# Семинар 2

# ЗАДАЧА 1
# Программа запрашивает у пользователя его фамилию, имя, отчество, введенные в
# одну строчку через пробел, и выводит на экран сообщения в 3 строки

fio = input("Введите Ваши ФИО: ")
surname, name, patronymic = fio.split()

print("Ваша фамилия:", surname)
print("Ваше имя:", name)
print("Ваше отчество:", patronymic)


# ЗАДАЧА 2
# Программа берет строку "1; 2; 3; 100" и возвращает:
# - список из целых чисел
# - список из чисел с плавающей точкой

input_string = "1; 2; 3; 100"

integer_list = [int(num) for num in input_string.split(";")]
float_list = [float(num) for num in input_string.split(";")]

print("Список целых чисел:", integer_list)
print("Список чисел с плавающей точкой:", float_list)


# ЗАДАЧА 3
# Программа запрашивает у пользователя номер мобильного телефона, введенный
# через дефис, а возвращает номер, записанный без дефисов и пробелов.

phone_number = input("Введите номер телефона в формате 8-900-123-45-67: ")
cleaned_number = phone_number.replace("-", "").replace(" ", "")

print("Номер телефона без дефисов и пробелов:", cleaned_number)


# ЗАДАЧА 4
# Запрос списка с клавиатуры

# Программа принимает на вход список L, в котором хранятся значения доходов
# домохозяйств за месяц, а возвращает новый список L2 ‒ список
# логарифмированных значений доходов.

import math
# Ввод списка L с клавиатуры через пробел
L = input().split()
# Создание списка L2 с логарифмированными значениями доходов
L2 = [math.log(float(x)) for x in L]
# Вывод списка L2
print(L2)

# 2-й вариант, если список уже дан
import math


def logarifmirovat_spisok(L):
    L2 = [math.log(x) for x in L]
    return L2


# Пример использования программы
L = [1000, 2000, 3000, 4000, 5000]
L2 = logarifmirovat_spisok(L)
print(L2)


# ЗАДАЧА 5
# Напишите программу, которая принимает на вход список слов такого вида:
# words = ["Speak ","to", "me ", "of", "Florence" ,"And ", "of", "the",
# "Renaissance"] а возвращает список
# words_clean = ["speak", "to", "me", "of", "florence", "and", "of", "the",
# "renaissance"]
# Другими словами, программа убирает пробелы в словах и приводит все слова к
# нижнему регистру.
# Подсказка: запросите help() по методам strip() и lower().


def clean_words(words):
    words_clean = []
    for word in words:
        word_clean = word.strip().lower()
        words_clean.append(word_clean)
    return words_clean


# Пример использования программы
words = ["Speak ", "to", "me ", "of", "Florence", "And ", "of", "the",
         "Renaissance"]
words_clean = clean_words(words)
print(words_clean)
