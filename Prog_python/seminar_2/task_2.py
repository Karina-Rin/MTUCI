# Программа берет строку "1; 2; 3; 100" и возвращает:
# - список из целых чисел
# - список из чисел с плавающей точкой

input_string = "1; 2; 3; 100"

integer_list = [int(num) for num in input_string.split(";")]
float_list = [float(num) for num in input_string.split(";")]

print("Список целых чисел:", integer_list)
print("Список чисел с плавающей точкой:", float_list)
