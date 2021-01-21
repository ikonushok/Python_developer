from math import factorial as fact  # импорт метода факториал


def c(n, k):
    """
    Количество сочетаний k элементов из n
    Биномиальный коэффициент
    """
    return fact(n) / (fact(n - k) * fact(k))

print(c(4, 2))
print(c(10, 3))

assert c(4, 2) == 6
assert c(10, 3) == 8, 'Не все в порядке!'