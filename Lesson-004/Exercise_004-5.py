# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


def creat_dict(polynomial):
    dict_polynomial = {}
    polynomial = polynomial.replace(' - ', ' -').replace(' + ', ' +')
    polynomial = polynomial.split()
    polynomial = polynomial[:-2]
    for i in range(len(polynomial)):
        polynomial[i] = polynomial[i].replace('+', '').split('x^')
        dict_polynomial[int(polynomial[i][1])] = int(polynomial[i][0])
    return dict_polynomial


def sum_pol(dict1, dict2):
    dict_result = {}
    maximum = (max(max(dict1), max(dict2)))
    for i in range(maximum, -1, -1):
        first = dict1.get(i)
        second = dict2.get(i)
        if first != None or second != None:
            dict_result[i] = (first if first != None else 0) + (second if second != None else 0)
    return dict_result


def result_polinomyal(dict_result):
    result = ''
    for i in dict_result.items():
        if result == '':
            if i[1] < 0:
                result += ' - ' + str(abs(i[1])) + 'x^' + str(abs(i[0]))
            else:
                result += str(abs(i[1])) + 'x^' + str(abs(i[0]))
        else:
            if i[1] < 0:
                result += ' - ' + str(abs(i[1])) + 'x^' + str(abs(i[0]))
            else:
                result += ' + ' + str(abs(i[1])) + 'x^' + str(abs(i[0]))
    result = result.replace('x^1', 'x').replace('x^0', '')
    result += ' = 0'
    return result


with open('result_004-1.txt', 'r') as text:
    polynomial1 = text.readline()

with open('result_004-2.txt', 'r') as text:
    polynomial2 = text.readline()

dict_polinomial1 = creat_dict(polynomial1)
dict_polinomial2 = creat_dict(polynomial2)
dict_result = sum_pol(dict_polinomial1, dict_polinomial2)
result = result_polinomyal(dict_result)

with open('Result.txt', 'w') as text:
    text.writelines(result)
