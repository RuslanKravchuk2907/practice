greeting = 'Hello, World!'
print(greeting)

line01 = "********************"
line01 = "********************"
line01 = "********************"

import math


def get_plan(current_production: int, months: int, percent: int) -> list:
    production_plan = []  # Ініціалізуємо список для зберігання плану виробництва

    for _ in range(months):
        # Додаємо до плану виробництва поточну кількість роботів для поточного місяця
        production_plan.append(current_production)
        # Збільшуємо поточну кількість роботів на величину відсотку
        current_production += current_production * percent / 100

    return list(map(math.floor, production_plan))


# Приклад використання:
current_production = 1000  # Починаємо рахунок від 1000, а не від 0
months = 6  # Збільшуємо кількість місяців на 1
percent = 35
print(get_plan(current_production, months, percent))