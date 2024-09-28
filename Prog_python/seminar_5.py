# Задание 1
def square(number):
    return number * number

def square_with_message(number):
    print(f"Квадрат числа равен: {number * number}")

def square_with_message_and_return(number):
    print(f"Квадрат числа равен: {number * number}")
    return number * number

a = square(2)
print(a)

square_with_message(3)

b = square_with_message_and_return(4)
print(b)

# Задание 2
def nums(n):
    return [n-1, n+1]

print(nums(7))  # [6, 8]

# Задание 3
def str_lower(string):
    words = string.split()  # Разделение строки на слова
    lower_words = [word.lower() for word in words]  # Преобразование слов в нижний регистр
    return lower_words


input_string = "В лесу родилась ёлочка В лесу она росла"
output_list = str_lower(input_string)
print(output_list)

# Задание 4
import math


def my_log(numbers):
    result = []
    for num in numbers:
        if num <= 0:
            result.append(None)
        else:
            result.append(math.log(num))
    return result


numbers = [1, 3, 2.5, -1, 9, 0, 2.71]
result = my_log(numbers)
print(result)

# Задание 5
def create_dict(names, ages):
    if len(names) == len(ages):
        return dict(zip(names, ages))
    else:
        print("Списки имеют разную длину")
        return {}


names = ["Ann", "Tim", "Sam"]
ages = [12, 23, 17]
result = create_dict(names, ages)
print(result)

names = ["Ann", "Tim", "Sam"]
ages = [12, 23, 17, 45]
result = create_dict(names, ages)
print(result)  # Списки имеют разную длину
print(result)  # {}

# Задание 6
from math import factorial

def binom(k,n):
    return factorial(n)//(factorial(k)*factorial(n-k))

def binom_prob(p, n, k):
    return binom(k, n) * (p ** k) * ((1 - p) ** (n - k))

p = 0.5
n = 10
k = 5
result = binom_prob(p, n, k)
print(result)

# Задание 7
def all_sort(*args):
    return sorted(args)

numbers = all_sort(7, 6, 1, 3, 8, 0, -2)
print(numbers)
