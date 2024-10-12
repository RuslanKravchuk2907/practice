

persons = ['kravchuk_1990', 'pavlov_1993', 'fedik_1994', 'Rapota_1994']

names = []

for person_name in persons:
    surname = person_name.split('_')[0]

    if surname.startswitch("a"):
        continue

    surname = surname.title()
    names.append(surname)

print(names)
