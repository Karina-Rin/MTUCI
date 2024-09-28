# Импорт необходимых библиотек
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Определение нечётких переменных
volume_water = ctrl.Antecedent(np.arange(0, 201, 1), "volume_water")
temperature_water = ctrl.Antecedent(np.arange(10, 102, 1), "temperature_water")
volume_coffee = ctrl.Antecedent(np.arange(5, 21, 1), "volume_coffee")
brewing_time = ctrl.Antecedent(np.arange(30, 181, 1), "brewing_time")
coffee_strength = ctrl.Consequent(np.arange(0, 101, 1), "coffee_strength")

# Определение функций принадлежности для каждой переменной
# Объем воды
volume_water["very_low"] = fuzz.trimf(volume_water.universe, [0, 0, 50])
volume_water["low"] = fuzz.trimf(volume_water.universe, [0, 50, 100])
volume_water["medium"] = fuzz.trimf(volume_water.universe, [50, 100, 150])
volume_water["high"] = fuzz.trimf(volume_water.universe, [100, 150, 200])

# Температура воды
temperature_water["cold"] = fuzz.trimf(temperature_water.universe, [10, 10, 20]
                                       )
temperature_water["warm"] = fuzz.trimf(temperature_water.universe, [10, 20, 45]
                                       )
temperature_water["hot"] = fuzz.trimf(temperature_water.universe, [20, 46, 98])
temperature_water["boiling"] = fuzz.trimf(temperature_water.universe, [
    45, 98, 101])
# Объем кофе
volume_coffee["low"] = fuzz.trimf(volume_coffee.universe, [5, 5, 10])
volume_coffee["medium"] = fuzz.trimf(volume_coffee.universe, [5, 10, 10])
volume_coffee["high"] = fuzz.trimf(volume_coffee.universe, [10, 15, 20])
volume_coffee["very_high"] = fuzz.trimf(volume_coffee.universe, [15, 20, 20])

# Время варки
brewing_time["short"] = fuzz.trimf(brewing_time.universe, [30, 30, 60])
brewing_time["medium"] = fuzz.trimf(brewing_time.universe, [30, 60, 120])
brewing_time["long"] = fuzz.trimf(brewing_time.universe, [60, 120, 120])
brewing_time["very_long"] = fuzz.trimf(brewing_time.universe, [120, 180, 180])

# Визуализация функций принадлежности
fig, ax = plt.subplots()

# 1) Если объем воды очень мало и температура воды холодная и объем кофе мало
# и время варки мало Крепость кофе - слабый
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [0, 0, 50]),
    label="Объем воды: Очень мало",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [10, 10, 20]),
    label="Температура воды: Холодная",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [5, 5, 10]),
    label="Объем кофе: Мало",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [30, 30, 60]),
    label="Время заваривания: Мало",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Слабый")
ax.legend()
plt.show()

# 2) Если объем воды мало и температура воды теплая и объем кофе средний и
# время варки среднее - слабый
fig, ax = plt.subplots()
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [0, 50, 100]),
    label="Объем воды: Мало",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [10, 20, 45]),
    label="Температура воды: Теплая",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [5, 10, 10]),
    label="Объем кофе: Средний",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [30, 60, 120]),
    label="Время варки: Среднее",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Слабый")
ax.legend()
plt.show()

# 3) Если объем воды средний и температура воды горячая и объем кофе много и
# время варки много - средний
fig, ax = plt.subplots()
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [50, 100, 150]),
    label="Объем воды: Средний",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [20, 46, 98]),
    label="Температура воды: Горячая",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [10, 15, 20]),
    label="Объем кофе: Много",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [60, 120, 120]),
    label="Время варки: Много",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Средний")
ax.legend()
plt.show()

# 4) Если объем воды много и температура воды кипяток и объем кофе очень много
# и время варки очень много - крепкий
fig, ax = plt.subplots()
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [100, 150, 200]),
    label="Объем воды: Много",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [45, 98, 101]),
    label="Температура воды: Кипяток",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [15, 20, 20]),
    label="Объем кофе: Очень много",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [120, 180, 180]),
    label="Время варки: Очень много",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Крепкий")
ax.legend()
plt.show()

# 5) Если объем воды очень мало и температура воды кипяток и объем кофе
# средний и время варки среднее - средний
fig, ax = plt.subplots()
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [0, 0, 50]),
    label="Объем воды: Очень мало",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [45, 98, 101]),
    label="Температура воды: Кипяток",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [5, 10, 10]),
    label="Объем кофе: Средний",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [30, 60, 120]),
    label="Время варки: Среднее",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Средний")
ax.legend()
plt.show()

# 6.1) Если объем воды очень мало и температура воды горячая и объем кофе
# много и время варки много - крепкий
fig, ax = plt.subplots()
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [0, 0, 50]),
    label="Объем воды: Очень мало",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [20, 46, 98]),
    label="Температура воды: Горячая",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [10, 15, 20]),
    label="Объем кофе: Много",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [60, 120, 120]),
    label="Время варки: Много",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Крепкий")
ax.legend()
plt.show()

# 6.2) Если объем воды очень мало и температура воды кипяток и объем кофе
# много и время варки много - крепкий
fig, ax = plt.subplots()
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [0, 0, 50]),
    label="Объем воды: Очень мало",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [45, 98, 101]),
    label="Температура воды: Кипяток",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [10, 15, 20]),
    label="Объем кофе: Много",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [60, 120, 120]),
    label="Время варки: Много",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Крепкий")
ax.legend()
plt.show()

# 7.1) Если объем воды очень мало и температура воды горячая и объем кофе
# очень много и время варки много - слишком крепкий
fig, ax = plt.subplots()
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [0, 0, 50]),
    label="Объем воды: Очень мало",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [20, 46, 98]),
    label="Температура воды: Горячая",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [15, 20, 20]),
    label="Объем кофе: Очень много",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [60, 120, 120]),
    label="Время варки: Много",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Слишком крепкий")
ax.legend()
plt.show()

# 7.2) Если объем воды очень мало и температура воды кипяток и объем кофе
# очень много и время варки много - слишком крепкий
fig, ax = plt.subplots()
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [0, 0, 50]),
    label="Объем воды: Очень мало",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [45, 98, 101]),
    label="Температура воды: Кипяток",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [15, 20, 20]),
    label="Объем кофе: Очень много",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [60, 120, 120]),
    label="Время варки: Много",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Слишком крепкий")
ax.legend()
plt.show()

# 8) Если объем воды очень мало и температура воды теплая и объем кофе
# средний и время варки среднее - слабый
fig, ax = plt.subplots()
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [0, 0, 50]),
    label="Объем воды: Очень мало",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [10, 20, 45]),
    label="Температура воды: Теплая",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [5, 10, 10]),
    label="Объем кофе: Средний",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [30, 60, 120]),
    label="Время варки: Среднее",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Слабый")
ax.legend()
plt.show()

# 9) Если объем воды очень мало и температура воды горячая и объем кофе
# много и время варки много - крепкий
fig, ax = plt.subplots()
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [0, 0, 50]),
    label="Объем воды: Очень мало",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [20, 46, 98]),
    label="Температура: Горячая",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [10, 15, 20]),
    label="Объем кофе: Много",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [60, 120, 120]),
    label="Время варки: Много",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Крепкий")
ax.legend()
plt.show()

# 10.1) Если объем воды очень мало и температура воды кипяток и объем кофе
# очень много и время варки много - слишком крепкий
fig, ax = plt.subplots()
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [0, 0, 50]),
    label="Объем воды: Очень мало",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [45, 98, 101]),
    label="Температура воды: Кипяток",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [15, 20, 20]),
    label="Объем кофе: Очень много",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [60, 120, 120]),
    label="Время варки: Много",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Слишком крепкий")
ax.legend()
plt.show()

# 10.2) Если объем воды очень мало и температура воды кипяток и объем кофе
# очень много и время варки очень много - слишком крепкий
fig, ax = plt.subplots()
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [0, 0, 50]),
    label="Объем воды: Очень мало",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [45, 98, 101]),
    label="Температура воды: Кипяток",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [15, 20, 20]),
    label="Объем кофе: Очень много",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [120, 180, 180]),
    label="Время варки: Очень много",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Слабый")
ax.legend()
plt.show()

# 11.1) Если объем воды средний и температура воды холодная и объем кофе мало
# и время варки мало - слабый
fig, ax = plt.subplots()
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [50, 100, 150]),
    label="Объем воды: Средний",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [10, 10, 20]),
    label="Температура воды: Холодная",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [5, 5, 10]),
    label="Объем кофе: Мало",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [30, 30, 60]),
    label="Время варки: Мало",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Слабый")
ax.legend()
plt.show()

# 11.2) Если объем воды средний и температура воды холодная и объем кофе мало
# и время варки среднее - слабый
fig, ax = plt.subplots()
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [50, 100, 150]),
    label="Объем воды: Средний",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [10, 10, 20]),
    label="Температура воды: Холодная",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [5, 5, 10]),
    label="Объем кофе: Мало",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [30, 60, 120]),
    label="Время варки: Среднее",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Слабый")
ax.legend()
plt.show()

# 11.3) Если объем воды средний и температура воды теплая и объем кофе мало и
# время варки мало - слабый
fig, ax = plt.subplots()
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [50, 100, 150]),
    label="Объем воды: Средний",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [10, 20, 45]),
    label="Температура воды: Теплая",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [5, 5, 10]),
    label="Объем кофе: Мало",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [30, 30, 60]),
    label="Время варки: Мало",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Слабый")
ax.legend()
plt.show()

# 11.4) Если объем воды средний и температура воды теплая и объем кофе мало и
# время варки среднее - слабый
fig, ax = plt.subplots()
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [50, 100, 150]),
    label="Объем воды: Средний",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [10, 20, 45]),
    label="Температура воды: Теплая",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [5, 5, 10]),
    label="Объем кофе: Мало",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [30, 60, 120]),
    label="Время варки: Среднее",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Слабый")
ax.legend()
plt.show()

# 12.1) Если объем воды средний и температура воды горячая и объем кофе
# средний и время варки много - крепкий
fig, ax = plt.subplots()
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [50, 100, 150]),
    label="Объем воды: Средний",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [20, 46, 98]),
    label="Температура: Горячая",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [5, 10, 10]),
    label="Объем кофе: Средний",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [60, 120, 120]),
    label="Время варки: Много",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Крепкий")
ax.legend()
plt.show()

# 12.2) Если объем воды средний и температура воды кипяток и объем кофе
# средний и время варки много - крепкий
fig, ax = plt.subplots()
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [50, 100, 150]),
    label="Объем воды: Средний",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [45, 98, 101]),
    label="Температура воды: Кипяток",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [5, 10, 10]),
    label="Объем кофе: Средний",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [60, 120, 120]),
    label="Время варки: Много",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Крепкий")
ax.legend()
plt.show()

# 13.1) Если объем воды много и температура воды холодная и объем кофе мало и
# время варки мало - слабый
fig, ax = plt.subplots()
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [100, 150, 200]),
    label="Объем воды: Много",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [10, 10, 20]),
    label="Температура воды: Холодная",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [5, 5, 10]),
    label="Объем кофе: Мало",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [30, 30, 60]),
    label="Время варки: Мало",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Слабый")
ax.legend()
plt.show()

# 13.2) Если объем воды много и температура воды теплая и объем кофе мало и
# время варки мало - слабый
fig, ax = plt.subplots()
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [100, 150, 200]),
    label="Объем воды: Много",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [10, 20, 45]),
    label="Температура воды: Теплая",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [5, 5, 10]),
    label="Объем кофе: Мало",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [30, 30, 60]),
    label="Время варки: Мало",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Слабый")
ax.legend()
plt.show()

# 14.1) Если объем воды много и температура воды горячая и объем кофе средний
# и время варки много - средний
fig, ax = plt.subplots()
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [100, 150, 200]),
    label="Объем воды: Много",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [20, 46, 98]),
    label="Температура воды: Горячая",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [5, 10, 10]),
    label="Объем кофе: Средний",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [60, 120, 120]),
    label="Время варки: Много",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Средний")
ax.legend()
plt.show()

# 14.2) Если объем воды много и температура воды кипяток и объем кофе средний
# и время варки много - средний
fig, ax = plt.subplots()
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [100, 150, 200]),
    label="Объем воды: Много",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [45, 98, 101]),
    label="Температура воды: Кипяток",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [5, 10, 10]),
    label="Объем кофе: Средний",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [60, 120, 120]),
    label="Время варки: Много",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Средний")
ax.legend()
plt.show()

# 15.1) Если объем воды много и температура воды кипяток и объем кофе много и
# время варки много - слишком крепкий
fig, ax = plt.subplots()
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [100, 150, 200]),
    label="Объем воды: Много",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [45, 98, 101]),
    label="Температура воды: Кипяток",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [10, 15, 20]),
    label="Объем кофе: Много",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [60, 120, 120]),
    label="Время варки: Много",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Слишком крепкий")
ax.legend()
plt.show()

# 15.2) Если объем воды много и температура воды кипяток и объем кофе очень
# много и время варки очень много - слишком крепкий
fig, ax = plt.subplots()
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [100, 150, 200]),
    label="Объем воды: Много",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [45, 98, 101]),
    label="Температура воды: Кипяток",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [15, 20, 20]),
    label="Объем кофе: Очень много",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [120, 180, 180]),
    label="Время варки: Очень много",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Слишком крепкий")
ax.legend()
plt.show()

# 15.3) Если объем воды много и температура воды кипяток и объем кофе много
# и время варки очень много - слишком крепкий
fig, ax = plt.subplots()
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [100, 150, 200]),
    label="Объем воды: Много",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [45, 98, 101]),
    label="Температура воды: Кипяток",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [10, 15, 20]),
    label="Объем кофе: Много",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [120, 180, 180]),
    label="Время варки: Очень много",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Слишком крепкий")
ax.legend()
plt.show()

# 15.4) Если объем воды много и температура воды кипяток и объем кофе очень
# много и время варки много - слишком крепкий
fig, ax = plt.subplots()
ax.plot(
    volume_water.universe,
    fuzz.trimf(volume_water.universe, [100, 150, 200]),
    label="Объем воды: Много",
)
ax.plot(
    temperature_water.universe,
    fuzz.trimf(temperature_water.universe, [45, 98, 101]),
    label="Температура воды: Кипяток",
)
ax.plot(
    volume_coffee.universe,
    fuzz.trimf(volume_coffee.universe, [15, 20, 20]),
    label="Объем кофе: Очень много",
)
ax.plot(
    brewing_time.universe,
    fuzz.trimf(brewing_time.universe, [60, 120, 120]),
    label="Время варки: Много",
)
ax.set_ylabel("Принадлежность")
ax.set_title("Крепость кофе - Слишком крепкий")
ax.legend()
plt.show()
