
def dividers_num(num):
    """
    выводит список всех делителей числа
    :param num:
    :return:
    """
    result = []
    for i in range(1, num//2 + 1):
        if num % i == 0:
            result.append(i)
    return result + [num]


def prime_simple(num):
    """
    проверка числа на простоту
    :param num:
    :return:
    """
    if dividers_num(num)[1] == num: print('Число простое')
    else: print('Число НЕ простое')


def prime_def(num):
    """
    Поиск максимального простого делителея числа
    :param num:
    :return:
    """
    from math import sqrt
    prime_set = set(range(1, num + 1))
    #print(prime_set)
    for i in range (2, int(sqrt(num))):
        if i in prime_set:
            prime_set -= set(range(2*i, num + 1, i))
    #print(prime_set)

    n = []
    for i in prime_set:
        if num % i == 0: n.append(i)

    return max(n)

#print(prime_def(21))

