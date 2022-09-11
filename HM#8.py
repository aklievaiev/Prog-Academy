# Exercise 1

week = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thuersday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}
day = int(input('Day: '))
print(week.get(day))

# Exercise 2

cat = {
    'animal': 'cat',
    'breed': 'sphynx',
    'wool': 'none',
    'name': 'Floki',
    'sex': 'male',
    'allergy': 'none',
    'adress': {
        'city': 'Kyiv',
        'street': 'Myropilska',
        'phone': '+380933706113'
    }
}

# Exercise 3

text = input('Text: ')
letters = set(text)
chars = {}

for item in letters:
    if not chars.get(item):
        chars[item] = text.count(item)

print(chars)