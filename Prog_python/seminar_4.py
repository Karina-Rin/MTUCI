# Задача 1
rept = {"python" : "питон",
        "anaconda" : "анаконда",
        "tortoize" : "черепаха"}

rept["snake"] = "змея"
rept["tortoise"] = rept.pop("tortoize")

for key, value in rept.items():
    print(f"{value} по-английски будет {key}.")

# Задача 2
cnt = ["Andorra", "Belarus", "Denmark", "Kenya", "Jamaica", "Romania"]
fh = [1.0, 6.0, 1.0, 4.0, 2.5, 2.0]
dictionary = dict(zip(cnt, fh))
print(dictionary)

# Задача 3
pairs = [(2, 4), (4, 6), (0, 1), (5, 2), (9, 1), (3, 8)]
calc = {}

for pair in pairs:
    product = pair[0] * pair[1]
    calc[pair] = product

print(calc)

# Задача 4
grades = {'Anna': 4, 'Bob': 3, 'Claire': 5, 'Dick': 2, 'Elena': 5, 'Fred': 5,
          'George': 4, 'Kristina': 3, 'Nick': 2, 'Ursula': 4, 'Viktor': 5}

for student, grade in grades.items():
    print(f"{student}: {grade}")

excel = []
good = []
satisf = []
bad = []

for student, grade in grades.items():
    if grade == 5:
        excel.append(student)
    elif grade == 4:
        good.append(student)
    elif grade == 3:
        satisf.append(student)
    else:
        bad.append(student)

print("Студенты с отличными оценками:")
for student in excel:
    print(student)

print("Студенты с хорошими оценками:")
for student in good:
    print(student)

print("Студенты с удовлетворительными оценками:")
for student in satisf:
    print(student)

print("Студенты с плохими оценками:")
for student in bad:
    print(student)
