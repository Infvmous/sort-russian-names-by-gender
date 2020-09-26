import json


def json_to_dict(filename):
    with open(filename, encoding='utf-8-sig') as f:
        return json.load(f)


def sort(names, all_names):
    male_names = []
    female_names = []
    for dicti in all_names:
        name = dicti['Name']
        if name in names:
            if dicti['Sex'] == 'Ж':
                female_names.append(name)
            else:
                male_names.append(name)
    return male_names, female_names


def main():
    names = ['Андрей', 'Елена', 'Юлия', 'Роберт', 'Валерия', 'Амбер']
    filename = 'russian_names.json'

    all_names = json_to_dict(filename)
    sorted_names = sort(names, all_names)

    print(sorted_names[0])
    print(sorted_names[1])


if __name__ == '__main__':
    main()