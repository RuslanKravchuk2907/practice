# Зроби рефакторинг коду, який ти бачиш на екрані:
#
# 1 Видали вже оголошену змінну result і не оголошуй нові.
# 2 Видали ключове слово elif і замінити на return так, щоб логіка функції не постраждала.
# 3 Не використовуй тернарний оператор.
def get_numbers_equality(a: int, b: int) -> str:

    if a == b:
        result = "a and b are equal"
    elif a < b:
        result = "a is less than b"
    elif a > b:
        result = "a is greater than b"

    return result


# Solution
def get_numbers_equality(a: int, b: int) -> str:
    if a == b:
        return "a and b are equal"
    if a < b:
        return "a is less than b"
    if a > b:
        return "a is greater than b"


# int
x1 = 42
print(f"{x1=}, {type(x1)=}")

x2 = 0b101010
print(f"{x2=}, {type(x2)=}")

x3 = 0o52
print(f"{x3=}, {type(x3)=}")

x4 = 0x2a   # 0x2A [0-9] [a-f] or [A-F]
print(f"{x4=}, {type(x4)=}")
print()


# float
y1 = 42.0
y2 = 42.
print(f"{y1=}, {type(y1)=}")

y3 = 0.42e2     # 0.42 * 10 ** 22
y4 = .42e2
print(f"{y3=}, {type(y3)=}")

y5 = 42_000_000e6       # 42_000_000 / 10 ** 6
print(f"{y5=}, {type(y5)=}")

# Century From Year
def get_century(year: int) -> int:
    if year <= 0:
        return 1  # Літочислення починається з 1 року н.е.

    # Визначення століття для року
    return (year - 1) // 100 + 1


print(get_century(2001))  # 21
print(get_century(0))  # 1
print(get_century(1786))  # 18
print(get_century(1500))  # 15


def is_even(number: float) -> bool:
    if not isinstance(number, int):
        return False
    return number % 2 == 0


print(is_even(100))
print(is_even(0))
print(is_even(77))
print(is_even(10.2))
print(is_even(-2))





# Get Rectangle Area
import math


def get_rectangle_area(side: int, diagonal: int) -> float | str:
    if side <= 0 or diagonal <= 0:
        return "not a rectangle"
    if diagonal <= side:
        return "not a rectangle"
    under_sqrt = diagonal**2 - side**2
    if under_sqrt <= 0:
        return "not a rectangle"
    other_side = math.sqrt(under_sqrt)
    area = side * other_side
    return round(area, 1)


print(get_rectangle_area(10, 20))
print(get_rectangle_area(9, 18))
print(get_rectangle_area(100, 98))
print(get_rectangle_area(-5, 10))
print(get_rectangle_area(0, 10))
print(get_rectangle_area(10, 0))


# number checker

import math


def number_checker(number: float) -> list:
    return [math.isinf(number), math.isnan(number)]


print(number_checker(1))                # [False, False]
print(number_checker(-1e10000))         # [True, False]
print(number_checker(float("nan")))     # [False, True]



# Make Decision
def make_decision(
    fuel_remaining: int,
    distance: int,
    fuel_consumption: float
) -> str:
    if fuel_remaining < 0 or distance < 0 or fuel_consumption <= 0:
        return "please, enter the valid data"
    required_fuel = (distance / 100) * fuel_consumption
    if fuel_remaining >= required_fuel:
        return "reach gas station by themselves"
    else:
        return "ask for help"


print(make_decision(5, 50, 0))
print(make_decision(-1, 50, 6.5))
print(make_decision(5, -50, 6.5))
print(make_decision(0, 0, 6.5))
print(make_decision(10, 50, 5))
print(make_decision(2, 50, 5))


# count networking

def count_networking(quarantine_length: int, frequency: int) -> int:
    # Якщо карантин триває весь рік або довше, вечірок не буде
    if quarantine_length >= 12:
        return 0

    # Перший місяць після завершення карантину
    start_month = quarantine_length + 1

    # Підраховуємо кількість вечірок
    party_count = 0
    for month in range(start_month, 13):
        if (month - start_month) % frequency == 0:
            party_count += 1

    return party_count


print(count_networking(0, 1))  # 12 (кожен місяць)
print(count_networking(3, 1))  # 9 (місяці 4-12)
print(count_networking(3, 2))  # 5 (місяці 4, 6, 8, 10, 12)
print(count_networking(12, 1))  # 0 (карантин на весь рік)
print(count_networking(11, 3))  # 1 (місяць 12)
print(count_networking(2, 5))  # 2 (місяці 3 і 8)
print(count_networking(3, 4))  # 3 (місяці 4, 8, 12)



# Generate Random List

import random


def generate_random_list(min_value: int, max_value: int, length: int) -> list:
    # Генеруємо список із випадковими числами заданої довжини
    return [random.randint(min_value, max_value) for _ in range(length)]


print(generate_random_list(1, 1, 1))   # [1]
print(generate_random_list(1, 3, 5))   # Наприклад, [2, 3, 1, 1, 3]
print(generate_random_list(-1, 1, 3))  # Наприклад, [0, -1, 1]



# For loop

sum_of_number = 0
#  Write code here
for number in range(5, 16):
    sum_of_number += number


print(sum_of_number)


sum_of_number = 0
#  Write code here
for number in range(5, 16, 2):
    sum_of_number += number


print(sum_of_number)


# Print the Progress

initial_distance = 5
increment = 2
total_weeks = 10

# Копія початкової дистанції для обчислень
current_distance = initial_distance

# Цикл для обчислення дистанції кожного тижня
for week in range(1, total_weeks + 1):
    print(current_distance)
    current_distance += increment

# Functions

def add_interest(balance, interest_rate):
    #  Write code here
    return balance * (1 + interest_rate / 100)


initial_balance = 1000
new_balance = add_interest(initial_balance, 5)
result_balance = add_interest(new_balance, 5)

print(result_balance)




def temperature(value):
    #  Write code here
    if value < 20:
        return "Cold"
    elif  20 <= value <= 50:
        return "Warm"
    else:
        return "Hot"
temperature(51)


# List + List
def get_lists_sum(lis1, lis2):
    # Повертаємо суму всіх елементів двох списків
    return sum(lis1) + sum(lis2)

# Приклади виклику функції
print(get_lists_sum([1, 2], [3, 4]))  # Виведе: 10
print(get_lists_sum([1, 2, 3, 4], [5, 6, 7, 8]))  # Виведе: 36
print(get_lists_sum([], []))