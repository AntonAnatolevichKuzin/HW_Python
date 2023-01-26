import work_with_data as wwd


def just_do_it():
    """Пользовательский интерфейс"""
    print('Добро пожаловать!\n\
    Что Вас интересует:\n\
    1 - Добавить контакты;\n\
    2 - Показать контакты;\n\
    3 - Найти контакт.')
    ch = input('Введите цифру: ')
    if ch == '1':
        sep = wwd.separator()
        wwd.import_data(wwd.input_data(), sep)
    elif ch == '2':
        data = wwd.export_data()
        print_data(data)
    elif ch == '3':
        word = input("Введите данные для поиска: ")
        data = wwd.export_data()
        item = wwd.search_data(word, data)
        if item != None:
            print('Фамилия'.center(20), 'Имя'.center(20),
                  'Телефон'.center(15), 'Примечание'.center(30))
            print("~"*85)
            print(item[0].center(20), item[1].center(20),
                  item[2].center(15), item[3].center(30))
        else:
            print("Таких данных нет!")
    else:
        print('Нет такого значения!')


def print_data(data):
    """Вывод на печать"""
    if len(data) > 0:
        print('Фамилия'.center(20), 'Имя'.center(20),
              'Телефон'.center(15), 'Примечание'.center(30))
        print("~"*85)
        for item in data:
            print(item[0].center(20), item[1].center(20),
                  item[2].center(15), item[3].center(30))
    else:
        print('Справочник пуст!')