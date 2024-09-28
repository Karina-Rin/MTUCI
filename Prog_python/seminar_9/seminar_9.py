import pandas as pd

# import matplotlib.pyplot as plt
# Загрузка базы данных из файла Titanic.csv
df = pd.read_csv("Titanic.csv", index_col="PassengerId")

# df.info()

# Удаление из базы строк с пропущенными значениями и сохранение изменения
df = df.dropna()
df
# Вывод сводной информации по базе данных: какие переменные в ней есть,
# какого они типа + сколько заполненных наблюдений в каждой столбце.


# 5 Выведите сводную статистическую информацию по каждому количественному
# показателю в базе (описательные статистике).
# df = df.describe()
# df

# Создание гистограммы для переменной Возраст (Age) красного цвета
# fig, ax = plt.subplots()
# ax.hist(df["Age"], color="red", bins=10)

# Настройка заголовка и меток осей
# ax.set_title("Возраст (Age)", size=20)
# ax.set_xlabel("Лет", size=14)
# ax.set_ylabel("Количество людей", size=14)

# Отображение графика
# plt.show()

# df = df["Fare"].describe()
# df
# Вывод первых строк базы данных без пропущенных значений

new_df = list(df.columns)
new_df[1] = "Class"
df.columns = new_df
df.columns


# female = df[df["Sex"] == "female"]
# female
# female.to_csv(r"female.csv", index = True, sep=";")

# print(list(df.columns))

# Ymale = df[(df["Sex"] == "male") & (df["Age"] < 32)]
# Ymale
# Ymale.to_csv(r"Ymale.csv", index = True, sep=";")

# print(female)
# print(Ymale)

# df = df[((df["Class"] == 1) | (df["Class"] == 2)) & (df["Survived"] == 1)]
# df

# print(df)

my_list = list(df["Sex"] == "female" if 1 else 0)
df["Female"] = my_list
df["Female"] = (
    df["Female"]
    .replace(to_replace=[True, False], value=[1, 0])
    .infer_objects(copy=False)
)

print(df)


# df = df["Embarked"].unique()
# print(df)

# df = df.groupby(["Survived"]).mean(numeric_only=True)
# print(df)
# data_sex = df.groupby('Sex').agg({'Age': ['mean', 'median']})
# data_sex
# print(data_sex)


column = list(df.columns)
d = dict(zip(column, [l.lower() for l in column]))
df = df.rename(columns=d)
print(df)


# print(df.head(893))

df.to_csv(r"Titanic-new.csv", index=True, sep=";")
