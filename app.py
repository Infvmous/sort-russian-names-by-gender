import json


names = ['Андрей', 'Елена', 'Юлия', 'Роберт', 'Валерия', 'Амбер']
male_names = []
female_names = []

filename = 'russian_names.json'

with open(filename, encoding='utf-8-sig') as f:
    data = json.load(f)

for dicti in data:
    name = dicti['Name']
    sex = dicti['Sex']
    if name in names and sex == 'Ж':
        female_names.append(name)
    elif name in names and sex == 'М':
        male_names.append(name)

print(male_names)
print(female_names)
