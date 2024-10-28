import pdb

# def add_numbers(a: int, b: int) -> int:
#     print(f"Adding {type(a)} and {type(b)}")
#     return a + b
#
#
# add_numbers(2, "3")


numbers = [1, "2", 3]

my_sum = 0

for number in numbers:
    pdb.set_trace()
    my_sum += number

    print(my_sum)
