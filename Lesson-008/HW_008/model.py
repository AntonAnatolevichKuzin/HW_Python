import view

student_id_counter = 0
students = {}
classes = {}


def AddNewStudent():
    new_student = dict()
    new_student['id'] = GetNewId()
    new_student['Last name'] = view.AddNewStudentInfo('Фамилию')
    new_student['First name'] = view.AddNewStudentInfo('Имя')
    new_student['Birthday'] = view.AddNewStudentInfo('Дату рождения')
    AddStudentsInClasses(new_student['id'])
    return new_student


def SaveFileStudents(student):
    with open('students.csv', 'a', encoding='UTF-8') as file:
        file.write(f"{student['id']}.{student['Last name']},{student['First name']};{student['Birthday']}\n")


def GetNewId():
    global student_id_counter
    student_id_counter += 1
    return student_id_counter


def AddStudentsInClasses(student_id):
    global classes
    student_class = view.AddNewStudentInfo('Какой класс')
    if student_class in classes:
        classes[student_class].append(student_id)
    else:
        classes[student_class] = [student_id]


def GetLastStudentId():
    global student_id_counter
    with open('students_id.txt', 'r', encoding='utf-8') as file:
        student_id_counter = int(file.read())


def SaveLastStudentId():
    global student_id_counter
    with open('students_id.txt', 'w', encoding='utf-8') as file:
        file.write(str(student_id_counter))


def SaveClasses():
    with open('classes.txt', 'a', encoding='utf-8') as file:
        for key, value in classes.items():
            file.write(key + ' - ' + str(value) + '\n')


def GetClasses():
    with open('classes.txt', 'r', encoding='UTF-8') as file:
        temp = file.readlines()
        classes = {}
        print(temp)
        for element in temp:
            classes[element[:element.index(' ')]] = element[element.index('[') + 1:-2].split(', ')
            print(classes)
        return classes


def GetStudents():
    with open('students.csv', 'r', encoding='UTF-8') as file:
        temp = file.readlines()
        students = {}
        for element in temp:
            students[element] = element.replace(',', ' ').replace(';', '. дата рождения: ')
            # print(students[element])
        return students


def Printing(data):
    for element in data:
        print(data[element])