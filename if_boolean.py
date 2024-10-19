# comparison operators
# !=
# <=
# >=
# not
# and
# or

password = "123"
user_input = "00000"

if (user_input == password) or (2 * 2 == 4):
    print('Welcome')
else:
    print('Wrong password')




s = "12345"

if len(s) == 8:
    print('Length 8')
elif len(s) == 6:
    print('Length 6')
else:
    print("zdorov")


password = "123"
user_input = "00000"

if user_input:
    if user_input == password:
        print('Welcome')
    else:
        print('Wrong password')
else:
    print('Enter password')


print('Welcome') if user_input else print('Wrong password')


# 1 - 100
# 3 - Fizz
# 5 - Buzz
# 3 & 5 FizzBuzz
# i

def fizz_buzz(i):
    if (i % 3 == 0) and (i % 5 == 0):
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

fizz_buzz(1)
fizz_buzz(2)
fizz_buzz(3)
fizz_buzz(5)
fizz_buzz(6)
fizz_buzz(8)
fizz_buzz(10)
fizz_buzz(15)
fizz_buzz(17)


work_done = True
day_finished = False

#  Write code here
can_go_home = work_done or day_finished

print(can_go_home)

