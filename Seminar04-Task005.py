
""" Даны два файла, в каждом из которых находится запись многочлена.
    Задача - сформировать файл, содержащий сумму многочленов.   """


def take_poly(file_count):
    poly = [open(f'poly-{i+1}.txt', 'r').read() for i in range(file_count)]
    return poly


def format_poly(poly):
    poly = [poly[i].replace(' ', '')[:-2] for i in range(len(poly))]
    poly = [poly[i].split('+') for i in range(len(poly))]
    return poly


def calc_poly(poly):
    sign = ['x^2', 'x', '']
    poly = [[p[i].replace('x^2', '').replace('x', '') for i in range(len(p))] for p in poly]
    poly = [int(poly[0][i]) + int(poly[1][i]) for i in range(len(poly[0]))]
    poly = [str(poly[i]) + sign[i] for i in range(len(poly))]
    poly = ' + '.join(poly)
    return poly


def save_poly(poly):
    filename = 'summa_poly.txt'
    open(filename, 'w', encoding='utf-8').write(poly)
    return print(f'Сумма многочленов сохранена в файл - {filename}')


summa_poly = calc_poly(format_poly(take_poly(2)))
print(f'Первый многочлен: {take_poly(2)[0]}')
print(f'Второй многочлен: {take_poly(2)[1]}')
print(f'Сумма многочленов: {summa_poly}')
save_poly(summa_poly)
