import json


names = ['Андрей', 'Елена', 'Юлия', 'Роберт', 'Валерия', 'Амбер']
male_names = []
female_names = []

filename = 'russian_names.json'

with open(filename, encoding='utf-8-sig') as f:
    data = json.load(f)

for dicti in data:
    name = dicti['Name']
    if name in names:
        if dicti['Sex'] == 'Ж':
            female_names.append(name)
        else:
            male_names.append(name)

print(male_names)
print(female_names)
