
""" Задана натуральная степень k. Сформировать случайным образом
    список коэффициентов (значения от 0 до 100) многочлена и записать
    в файл многочлен степени k.
    Пример:
        - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0   """

from random import randint


def rand_polynom(k):
    kff = [randint(0, 100) for _ in range(k + 1)]
    poly = [f'{kff[i]}x^{k - i}' for i in range(len(kff))]
    poly = ' + '.join(poly)
    poly += ' = 0'
    poly = poly.replace('x^1', 'x').replace('x^0', '').replace('0x', 'x')
    print(f'\nk={k} => {poly}')
    return poly


k = int(input('Введите натуральную степень k: '))

for i in range(1, 3):
    with open(f'poly-{i}.txt', 'w', encoding='utf-8') as file:
        file.write(rand_polynom(k))
        print(f'Полином сохранен в файл: poly-{i}.txt')
