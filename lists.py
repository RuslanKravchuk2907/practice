
persons = ['kravchuk_1990', 'pavlov_1993', 'fedik_1994', 'Rapota_1994']

# s_persons = sorted(persons)
# print(s_persons)

# function for sorted
def by_year(name):
    return name.split('_')[-1]

s_persons = sorted(persons, key=by_year)
print(s_persons)
