import view
import model


def Start():
    """Пользовательский интерфейс"""
    print('Добро пожаловать!\n\
    Что Вас интересует:\n\
    1 - Добавить нового ученика;\n\
    2 - Вывести список учеников;\n\
    3 - Вывести список классов')
    ch = input('Введите цифру: ')
    if ch == '1':
        model.GetLastStudentId()
        model.SaveFileStudents(model.AddNewStudent())
        model.SaveClasses()
        model.SaveLastStudentId()
    elif ch == '2':
        model.Printing(model.GetStudents())
    elif ch == '3':
        model.GetClasses()
