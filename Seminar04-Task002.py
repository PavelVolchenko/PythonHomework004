
""" Задайте натуральное число N. Напишите программу,
    которая составит список простых множителей числа N.  """


def prime_factors(number):
    lst = []
    i = 2
    print(number, "=", end=' ')
    while True:
        if number / i >= 1:
            if (number / i) % 2 == 0:
                lst.append(i)
                number /= i
            elif (number / i) % 2 == 1:
                lst.append(i)
                number /= i
            else:
                i += 1
        else:
            break
    print(' * '.join(map(str, lst)))


numbers = [52, 63, 128, 37, 5600, 750, 364]

for n in numbers:
    prime_factors(n)
