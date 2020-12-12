# Menu
def menu(num):
    """

    :param num:
    :return:
    """
    print(f'Доступная сумма: {num} руб.', end='\n\n')
    print('1. Пополнить счет')
    print('2. Совершить покупку')
    print('3. История покупок')
    print('4. Выход')
    ans = input('Введите номер пункта: ')
    return ans

# Покупка
def add(num, hist):
    """

    :param num:
    :param hist:
    :return:
    """
    sale = input('Введите сумму покупки: ')
    while not sale.replace('.', '', 1).isdigit():
        sale = input('Введите сумму покупки: ')
    sale = float(sale)
    if sale > num:
        print('Сумма покупки больше наличных денег')
    else:
        name = input('Введите название покупки: ')
        hist.append((name, sale))
        num -= sale
    return num, hist

# Перебор условий
# выбрать пункт меню
# пополнить счет
# проверив наличие денег, добавить расход
# вывести историю операций
# прерывание
num = 0
history = []
while True:
    # меню
    ans = menu(num)
    while ans not in ['1', '2', '3', '4']:
        ans = menu(num)

    # пополнение счета
    if ans == '1':
        amount = input('Введите сумму: ')
        while not amount.replace('.', '', 1).isdigit():
            amount = input('Введите сумму: ')
        num += float(amount)

    # покупки
    elif ans == '2':
       num, history = add(num, history)
    # выводим испорию покупок
    elif ans == '3':
        for name, sale in history:
            print(f'Было куплено {name} за {sale} руб.')

    else:  # иначе
        break  # выйти из основного цикла
