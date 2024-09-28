# Задача 1
number = float(input("Введите положительное число: "))

if number > 0:
    print("Молодец!")
else:
    print("Это не положительное число.")

# Задача 2
def print_grade_comment(grade):
    if grade < 1 or grade > 10:
        print("Ошибка: недопустимая оценка!")
        return

    print("Оценка:", grade)
    if grade <= 4:
        print("Плохо")
    elif grade <= 6:
        print("Удовлетворительно")
    elif grade <= 8:
        print("Хорошо")
    else:
        print("Отлично")


# Пример использования:
grades = [8, 6, 9, 4, 7]
for grade in grades:
    print_grade_comment(grade)

# Задача 3
password = "password123"  # Здесь нужно указать верный пароль

while True:
    user_input = input("Введите пароль: ")
    
    if user_input == password:
        print("Login success")
        break
    else:
        print("Incorrect password, try again!")

# Задача 4
favorites = [3, 7, 11, 23, 18, 48, 81]
user_input = int(input("Введите целое число: "))

if user_input in favorites:
    print("Мое любимое число!")
else:
    print("Эх, ну почему?")

# Задача 5
num = int(input("Введите число: "))

if num % 2 == 0:
    print("Это число чётное")
else:
    print("Это число нечётное")

# Задача 6
word = input("Введите существительное: ")

if word[0].isupper():
    print("Это имя собственное.")
else:
    print("Это имя нарицательное.")
