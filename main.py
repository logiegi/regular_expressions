import re
import csv
# Читаем адресную книгу в формате CSV в список contacts_list:
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# 1. Выполните пункты 1-3 задания.
def to_dict(contacts):
    contacts_update = {}
    contact_list = []
    for i in contacts:
        name, surname = i[0].split(), i[1].split()
        contact_list.append(name + surname + list(filter(None, i[2:])))
    for i in contact_list[1:]:
        if i[0] + ' ' + i[1] not in contacts_update:
            contacts_update[i[0] + ' ' + i[1]] = i[2:]
        else:
            for k in i[2:]:
                if k not in contacts_update[i[0] + ' ' + i[1]]:
                    contacts_update[i[0] + ' ' + i[1]].append(k)
                else:
                    pass
    return contacts_update


def change_number():
    text = []
    pattern = re.compile(r"(\+7|8)\s?\(?(\d{3})\)?\s?-?(\d{3})-?(\d{2})(-)?(\d+)\s?\(?(доб.)?\s?(\d+)?\)?")
    subst_pattern = r"+7(\2)\3-\4-\6 \7\8"
    for k, v in to_dict(contacts_list).items():
        text += [k.split() + [pattern.sub(subst_pattern, value) for value in v]]
    return text


# 2. Сохраните получившиеся данные в другой файл.
# Код для записи файла в формате CSV:
if __name__ == '__main__':
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(change_number())
