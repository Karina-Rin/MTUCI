# Модель общая. На выходе получаем значение переменной "Крепость кофе: "
# из вариантов: Слабый, Средний, Крепкий или Слишком крепкий.
# Импорт необходимых библиотек
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

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
temperature_water["boiling"] = fuzz.trimf(temperature_water.universe, [45, 98,
                                                                       101])
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

# Выходная переменная - крепость кофе
coffee_strength["weak"] = fuzz.trimf(coffee_strength.universe, [0, 0, 1])
coffee_strength["medium"] = fuzz.trimf(coffee_strength.universe, [0, 1, 2])
coffee_strength["strong"] = fuzz.trimf(coffee_strength.universe, [1, 2, 3])
coffee_strength["very_strong"] = fuzz.trimf(coffee_strength.universe, [2, 3, 3]
                                            )
# Определение базы правил
rules1 = ctrl.Rule(
    volume_water["very_low"]
    & temperature_water["cold"]
    & volume_coffee["low"]
    & brewing_time["short"],
    coffee_strength["weak"],
)
rules2 = ctrl.Rule(
    volume_water["low"]
    & temperature_water["warm"]
    & volume_coffee["medium"]
    & brewing_time["medium"],
    coffee_strength["weak"],
)
rules3 = ctrl.Rule(
    volume_water["medium"]
    & temperature_water["hot"]
    & volume_coffee["high"]
    & brewing_time["long"],
    coffee_strength["medium"],
)
rules4 = ctrl.Rule(
    volume_water["high"]
    & temperature_water["boiling"]
    & volume_coffee["very_high"]
    & brewing_time["very_long"],
    coffee_strength["strong"],
)
rules5 = ctrl.Rule(
    volume_water["very_low"]
    & temperature_water["boiling"]
    & volume_coffee["medium"]
    & brewing_time["medium"],
    coffee_strength["medium"],
)
rules6 = ctrl.Rule(
    volume_water["very_low"] & temperature_water["hot"]
    | temperature_water["boiling"] & volume_coffee["high"] &
    brewing_time["long"],
    coffee_strength["strong"],
)
rules7 = ctrl.Rule(
    volume_water["very_low"] & temperature_water["hot"]
    | temperature_water["boiling"] & volume_coffee["very_high"] &
    brewing_time["long"],
    coffee_strength["very_strong"],
)
rules8 = ctrl.Rule(
    volume_water["very_low"]
    & temperature_water["warm"]
    & volume_coffee["medium"]
    & brewing_time["medium"],
    coffee_strength["weak"],
)
rules9 = ctrl.Rule(
    volume_water["very_low"]
    & temperature_water["hot"]
    & volume_coffee["high"]
    & brewing_time["long"],
    coffee_strength["strong"],
)
rules10 = ctrl.Rule(
    volume_water["very_low"]
    & temperature_water["boiling"]
    & volume_coffee["very_high"]
    & brewing_time["long"]
    | brewing_time["very_long"],
    coffee_strength["very_strong"],
)
rules11 = ctrl.Rule(
    volume_water["medium"] & temperature_water["cold"]
    | temperature_water["warm"] & volume_coffee["low"] & brewing_time["short"]
    | brewing_time["medium"],
    coffee_strength["weak"],
)
rules12 = ctrl.Rule(
    volume_water["medium"] & temperature_water["hot"]
    | temperature_water["boiling"] & volume_coffee["medium"] &
    brewing_time["long"],
    coffee_strength["strong"],
)
rules13 = ctrl.Rule(
    volume_water["high"] & temperature_water["cold"]
    | temperature_water["warm"] & volume_coffee["low"] & brewing_time["short"],
    coffee_strength["weak"],
)
rules14 = ctrl.Rule(
    volume_water["high"] & temperature_water["hot"]
    | temperature_water["boiling"] & volume_coffee["medium"] &
    brewing_time["long"],
    coffee_strength["medium"],
)
rules15 = ctrl.Rule(
    volume_water["high"] & temperature_water["boiling"] & volume_coffee["high"]
    | volume_coffee["very_high"] & brewing_time["long"]
    | brewing_time["very_long"],
    coffee_strength["very_strong"],
)

# Создание системы нечеткого вывода
coffee_ctrl = ctrl.ControlSystem(
    [
        rules1,
        rules2,
        rules3,
        rules4,
        rules5,
        rules6,
        rules7,
        rules8,
        rules9,
        rules10,
        rules11,
        rules12,
        rules13,
        rules14,
        rules15,
    ]
)

# Создание симулятора
coffee_strength_prediction = ctrl.ControlSystemSimulation(coffee_ctrl)

# Задание входных переменных
coffee_strength_prediction.input["volume_water"] = 50
coffee_strength_prediction.input["temperature_water"] = 98
coffee_strength_prediction.input["volume_coffee"] = 15
coffee_strength_prediction.input["brewing_time"] = 120

# Вычисление значения выходной переменной
coffee_strength_prediction.compute()

# Получение значения выходной переменной
strength_value = coffee_strength_prediction.output["coffee_strength"]

# Вывод текстового значения
if strength_value < 1:
    strength_text = "слабый"
elif strength_value < 2:
    strength_text = "средний"
elif strength_value < 3:
    strength_text = "крепкий"
else:
    strength_text = "слишком крепкий"

print(f"Крепость кофе: {strength_text}")
