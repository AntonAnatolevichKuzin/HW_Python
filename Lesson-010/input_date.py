num_1 = 0
num_2 = 0
oper = ''


def inp(num_1, num_2):
    if 'j' in num_1 or 'j' in num_2:
        num_1 = complex(num_1)
        num_2 = complex(num_2)
    else:
        num_1 = float(num_1)
        num_2 = float(num_2)

    return (num_1, num_2)
