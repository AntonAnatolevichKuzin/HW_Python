
def export_data():
    """Считывание данных из файла"""
    with open('phone_book.csv', 'r', encoding='UTF-8') as file:
        data = []
        t = []
        for line in file:
            if ',' in line:
                temp = line.strip().split(',')
                data.append(temp)
            elif ';' in line:
                temp = line.strip().split(';')
                data.append(temp)
            elif ':' in line:
                temp = line.strip().split(':')
                data.append(temp)
            elif line != '':
                if line != '\n':
                    t.append(line.strip())
                else:
                    data.append(t)
                    t = []
    return data


def import_data(data, sep=None):
    """Запись данных в файл"""
    with open('phone_book.csv', 'a+', encoding='UTF-8') as file:
        if sep == None:
            for i in data:
                file.write(f"{i}\n")
            file.write(f"\n")
        else:
            file.write(sep.join(data))
            file.write(f"\n")


def search_data(word, data):
    """Поиск контактов"""
    if len(data) > 0:
        for item in data:
            if word in item:
                return item
    else:
        return None


def separator():
    """Вид разделителя для работы с данными разных форматов"""
    sep = input("Введите разделитель не более одного знака: ")
    while  len(sep) > 1:
        sep = input("Разделитель превышает допустимую днину, введите еще раз: ")
    if sep == "":
        sep = None
    return sep


def input_data():
    """Добавить контакт"""
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    note = input('Введите примечание: ')
    if note == '':
        note = '-'
    return [last_name, first_name, phone_number, note]

