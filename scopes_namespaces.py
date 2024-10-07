
# Namespaces

name = "Ruslan"

def a():
    name = "Kravchuk"
    age = 34
    print("Function a() namespace:", locals())

print("External namespace:", locals())

print()

a()


# Scope

name = "Ruslan"

def a():
    name = "Petrovich"

    def b():
        name = "Kravchuk"
        age = 34
        print(name)
        print(locals())

    b()

a()
