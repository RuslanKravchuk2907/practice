# def calculate_average(numbers):
#     total = 0
#     count = len(numbers)
#     for number in numbers:
#         total += number
#
#     if count > 0:
#         return total / count
#
#     return 0


# user_input = "   username@example.com   "
#
# #  Write code here
# cleaned_input = user_input.strip()
# left_strip_input = user_input.lstrip()
# right_strip_input = user_input.rstrip()
#
#
# print(user_input)
# print(cleaned_input )
# print(left_strip_input)
# print(right_strip_input)


# def count_substring(sentence: str, substring: str) -> int:
#     #  Write code here
#     count = sentence.count(substring)
#
#
# print(count_substring("Thank you for coming! Thank you for being with us!", "Thank you"))
#
# print(count_substring("I love my job because it gives me satisfaction", "love"))
#
#
# def weekday_order(weekday: str) -> int:
#     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#     return days.index(weekday)
#
# def sort_weekdays(weekdays: list) -> list:
#     return sorted(weekdays, key=weekday_order)


african_animals = ["Lion", "Leopard", "Elephant", "Rhinoceros", "Giraffe"]
new_african_animals = ["Hippo", "Gorilla"]
european_animals = ["Brown Bear", "Wild Boar", "Polar Bear", "Red Deer"]
# write your code below
animals = african_animals + new_african_animals
animals.extend(european_animals)

print(animals)
