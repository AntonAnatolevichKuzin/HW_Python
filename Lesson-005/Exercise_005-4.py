# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def encode(s):
    encoding = ''
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + s[i]
        i = i + 1
    return encoding

def decode(s):
    decoding = ''
    count = ''
    for elem in s:
        if elem.isdigit():
            count += elem
        else:
            decoding += int(count) * elem
            count = ''
    return decoding




if __name__ == '__main__':

    with open('data.txt', 'r') as text:
        init_data = text.readline()

    compress_data = encode(init_data)
    print(compress_data)
    decompress_data = decode(compress_data)
    print(decompress_data)
    
    with open('result.txt', 'w') as text:
        text.writelines(decompress_data)