def find_max(numbers):
    if not numbers:
        return None  # Повертаємо None, якщо список порожній

    max_num = numbers[0]  # Ініціалізуємо max_num першим елементом списку
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


# Тести функції
print(find_max([3, 5, 7, 2, 8]))  # Виведе: 8
print(find_max([-10, -5, -1, -20]))  # Виведе: -1
print(find_max([42]))  # Виведе: 42
print(find_max([]))  # Виведе: None

