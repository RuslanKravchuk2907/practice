# rating = 100

# print('Leon', rating)

# print('Leon', rating )

# print('Leon', 100)

# name = "Leon"
# number = 100

# result = f'{name} - {number}'

# print(result)


# string_var = 'Ruslan'
# integer_var = 34
# float_var = 34.0
# bool_var = True
# list_var = [1, 2, 3]
# dict_var = {"name": "Ruslan", "age": "34"}
# tuple_var = (1, 2, 3)
# none_var = None
#
#
# print(integer_var > 20)
# print(float_var < 10)
# print(integer_var == 42)
# print(string_var == "Hello, Python!")
# print(string_var > "Aloha")
# print(bool_var == True)
# print(bool_var != False)
# print(list_var == [1, 2, 3])
# print(list_var != [1, 2])
# print(list_var > [1, 2, 3])
# print(dict_var == {"name": "Ruslan", "age": "34"})
# print(dict_var != {"name": "Ruslan"})
# print(tuple_var == (1, 2, 3))
# print(tuple_var < (2, 3, 4))
# print(integer_var == float_var)
# print(string_var == bool_var)
# print(none_var == None)


# num_str = 125
# print(str(num_str))

# list_append = [1, 2, 3]
# list_append.append(4)
# list_append.append(5)
# print(list_append)
# print(len(list_append))
#
#
# list_extend = [4, 5, 6]
# list_extend.extend([7, 8, 9])
# print(list_extend)
# print(list_extend.index(6))


# dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
#
#
# print(dict_test['car'])
# print(dict_test['where'])
# print(dict_test.keys())
# print(dict_test.values())
# print(dict_test.items())


# correct_password = "password123"
# password = "password123"
#
# if password == correct_password:
#     print("Ви увійшли в систему")
# else:
#     print("Неправильний пароль")


days_of_week = 6

if days_of_week == 1:
    print("Its Monday")
elif days_of_week == 2:
    print("Its Tuesday")
elif days_of_week == 3:
    print("Its Wednesday")
elif days_of_week == 4:
    print("Its Thursday")
elif days_of_week == 5:
    print("Its Friday")
elif days_of_week == 6:
    print("Its Saturday")
elif days_of_week == 7:
    print("Its Sunday")
else:
    print("Go to work :)")

number = 5

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


numbers = [1, 2, 3, 4, 5, 6]

total_sum = 0
for num in numbers:
    total_sum += num

print(f"Сума чисел: {total_sum}")

number = 5

factorial = 1
for i in range(1, number + 1):
    factorial *= i

print(f"Факторіал числа {number}: {factorial}")


number = 5

for num in range(1, 51):
    if num % 2 == 0:
        print(num, end=" ")



start = 1
end = 50

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")