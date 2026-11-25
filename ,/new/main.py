person = {
    'name': 'Andria',
    'surname': 'Bochorishvili',
    'age': 14,
    'city': 'Rustavi',
    'profession': 'Footballer'
}

print('Full object:')

print(person)

print('-' * 30)


print('Only keys:')

print(person.keys())

print('-' * 30)


print('Only values:')

print(person.values())

print('-' * 30)


print('All keys and values:')

for key, value in person.items():
    print(f'{key}: {value}')



# 2 davaleba

book = {
    'title': 'Vefkhistkaosani',
    'author': 'Shota Rustaveli',
    'century': '12th',
    'verses': 1669,
    'genre': 'Epic poem'
}

book['century'] = '12th-13th'
book['verses'] = 1576

book['translator'] = 'Marjory Wardrop'
book['language'] = 'Georgian'

del book['genre']

print(book)
































