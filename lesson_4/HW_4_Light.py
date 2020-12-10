from random import randint
from collections import defaultdict

source = ['Иван', "Сергей", "Радмир", "Елена", "Ефим",
          "Дмитрий", "Ирина", "Федор", "Семен", "Кузьма", "Федот", "Анна", "Фёкла"]

def random_name(list_name, n=100):
    """

    :param list_name:
    :param n:
    :return:
    """
    result = []
    for i in range(n):
        idx = randint(0, len(list_name)-1)
        result.append(list_name[idx])
    return result

list_name = random_name((source))
#print(list_name)


def counter_name(list_name):
    """

    :param list_name:
    :return:
    """
    result = defaultdict(int)
    for i in list_name:
        result[i] += 1
    result = list(result.items())
    result.sort(key=lambda x: x[1], reverse=True)
    return result[0][0]

print(counter_name(list_name))


def rare_letter(list_name):
    """

    :param list_name:
    :return:
    """
    result = defaultdict(int)
    for i in list_name:
        result[i[0]] += 1
    result = list(result.items())
    result.sort(key=lambda x: x[1])
    return result[0][0]

print(rare_letter(list_name))
