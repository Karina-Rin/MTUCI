# Задача 1
# А
def multiply_number(number):
    return number * (variant_number + 7)

variant_number = 8
numbers = [12, 24, 36, 48, 109, 187]
result = list(map(multiply_number, numbers))

print(result)

# В
variant_number = 9
numbers = [12, 24, 36, 48, 109, 187]
result = list(map(lambda number: number * (variant_number + 7), numbers))

print(result)

# Задача 2
phone_number1 = [1, 2, 3, 4, 5]
phone_number2 = [6, 7, 8, 9, 10]
result = list(map(lambda x, y: x * y, phone_number1, phone_number2))

print(result)

# Задача 3
phone_number = "79671704909"  # номер телефона
variant_number = 3  # Зномер варианта

# Создание списка чисел и цифр номера телефона
number_list = [int(digit) * variant_number for digit in phone_number]
print(number_list)

# Фильтрация списка с использованием функции filter() и лямбда-функции
even_numbers = list(filter(lambda x: x % 2 == 0, number_list))
odd_numbers = list(filter(lambda x: x % 2 != 0, number_list))

print(even_numbers)
print(odd_numbers)

# Задача 3
phone_number = "79671704909"
variant_number = 5

# Применение целочисленного деления
integer_division_result = list(map(lambda x: int(x) // variant_number, phone_number))

# Применение дробного деления
float_division_result = list(map(lambda x: int(x) / variant_number, phone_number))

print("Результат целочисленного деления:", integer_division_result)
print("Результат дробного деления:", float_division_result)
