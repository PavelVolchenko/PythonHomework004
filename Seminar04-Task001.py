
""" Вычислить число c заданной точностью d
    Пример:
    - при d = 0.001, π = 3.141   10^{-1} ≤ d ≤10^{-10}    """

import math


def rnd(dn):
    if dn >= 0.0001:
        dn = len(str(dn)) - 1
        return '.' + str(dn) + 'g'
    else:
        dn = str(dn).split('-')[1]
        dn = int(dn) + 1
        return '.' + str(dn) + 'g'


d = [0.01, 0.0001, 0.0000001, 0.0000000001]
[print(f'- при d = {i}, π =', *[format(math.pi, rnd(i))]) for i in d]
