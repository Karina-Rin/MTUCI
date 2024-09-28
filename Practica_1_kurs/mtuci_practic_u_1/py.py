import os

# Получение текущего рабочего каталога
current_directory = os.getcwd()

# Вывод структуры каталогов в терминале
for root, dirs, files in os.walk(current_directory):
    level = root.replace(current_directory, '').count(os.sep)
    indent = ' ' * 4 * (level)
    print('{}{}/'.format(indent, os.path.basename(root)))
    sub_indent = ' ' * 4 * (level + 1)
    for f in files:
        print('{}{}'.format(sub_indent, f))

# Сохранение структуры каталогов в файл
with open('directory_structure.txt', 'w') as file:
    for root, dirs, files in os.walk(current_directory):
        level = root.replace(current_directory, '').count(os.sep)
        indent = ' ' * 4 * (level)
        file.write('{}{}/\n'.format(indent, os.path.basename(root)))
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            file.write('{}{}\n'.format(sub_indent, f))
