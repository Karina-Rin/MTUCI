# Функции принадлежности по входным переменным.
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Определение диапазонов и функций принадлежности для объема воды
volume_range = np.arange(0, 250, 1)

very_low = fuzz.trimf(volume_range, [0, 0, 50])
low = fuzz.trimf(volume_range, [0, 50, 100])
medium = fuzz.trimf(volume_range, [50, 100, 150])
high = fuzz.trimf(volume_range, [100, 150, 200])

# Определение диапазонов и функций принадлежности для температуры воды
temperature_range = np.arange(0, 110, 1)

cold = fuzz.trapmf(temperature_range, [0, 0, 10, 20])
warm = fuzz.trapmf(temperature_range, [10, 20, 45, 55])
hot = fuzz.trapmf(temperature_range, [45, 55, 98, 105])
boiling = fuzz.trapmf(temperature_range, [98, 105, 110, 110])

# Определение диапазонов и функций принадлежности для объема кофе
coffee_range = np.arange(0, 250, 1)

low = fuzz.trimf(coffee_range, [0, 0, 50])
medium = fuzz.trimf(coffee_range, [0, 50, 100])
high = fuzz.trimf(coffee_range, [50, 100, 150])
very_high = fuzz.trimf(coffee_range, [100, 150, 200])

# Определение диапазонов и функций принадлежности для времени варки
brewing_time_range = np.arange(0, 180, 1)

short = fuzz.trimf(brewing_time_range, [0, 0, 30])
medium_brewing = fuzz.trimf(brewing_time_range, [0, 30, 60])
long = fuzz.trimf(brewing_time_range, [30, 60, 120])
very_long = fuzz.trimf(brewing_time_range, [60, 120, 180])

# Визуализация функций принадлежности
fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=4, figsize=(8, 10))

ax0.plot(volume_range, very_low, "b", linewidth=1.5, label="Очень мало")
ax0.plot(volume_range, low, "g", linewidth=1.5, label="Малый")
ax0.plot(volume_range, medium, "r", linewidth=1.5, label="Средний")
ax0.plot(volume_range, high, "m", linewidth=1.5, label="Много")
ax0.set_title("Объем воды")
ax0.legend()

ax1.plot(temperature_range, cold, "b", linewidth=1.5, label="Холодная")
ax1.plot(temperature_range, warm, "g", linewidth=1.5, label="Теплая")
ax1.plot(temperature_range, hot, "r", linewidth=1.5, label="Горячая")
ax1.plot(temperature_range, boiling, "m", linewidth=1.5, label="Кипяток")
ax1.set_title("Температура воды")
ax1.legend()

ax2.plot(coffee_range, low, "b", linewidth=1.5, label="Мало")
ax2.plot(coffee_range, medium, "g", linewidth=1.5, label="Средний")
ax2.plot(coffee_range, high, "r", linewidth=1.5, label="Много")
ax2.plot(coffee_range, very_high, "m", linewidth=1.5, label="Очень много")
ax2.set_title("Объем кофе")
ax2.legend()

ax3.plot(brewing_time_range, short, "b", linewidth=1.5, label="Мало")
ax3.plot(brewing_time_range, medium_brewing, "g", linewidth=1.5,
         label="Среднее")
ax3.plot(brewing_time_range, long, "r", linewidth=1.5, label="Много")
ax3.plot(brewing_time_range, very_long, "m", linewidth=1.5, label="Очень много"
         )
ax3.set_title("Время варки")
ax3.legend()

plt.tight_layout()
plt.show()
