from math import factorial as fact

def p(n):
    """
    Число возможных перестановок
    :param n:
    :return:
    """
    return fact(n)

def c(n, m):
    """
    Число перстановок m из n
    :param n:
    :param m:
    :return:
    """
    return fact(n) / (fact(n-m)*fact(m))


def bernully(n, m, p):
    """
    Выпадение k из n с вероятностью p
    :param n:
    :param k:
    :param p:
    :return:
    """
    return c(n, m)*(p**m)*(1-p)**(n-m)

#print(bernully(20, 20, 0.5))