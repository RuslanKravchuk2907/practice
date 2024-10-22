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