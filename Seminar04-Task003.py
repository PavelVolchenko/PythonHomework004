
""" Задайте последовательность чисел. Напишите программу, которая
    выведет список неповторяющихся элементов исходной последовательности.   """

digits = [1, 2, 4, 5, 3, 2, 1, 1, 2, 4, 5, 7, 8]
dct = {}
for k in set(digits):
    dct.setdefault(k, digits.count(k))
print(f'Неповторяющиеся элементы:', end=' ')
for k, v in dct.items():
    if int(v) == 1:
        print(k, end=' ')
