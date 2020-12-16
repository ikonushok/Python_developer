from lesson_5.ultrapro import account, number, viktorina

while True:  # запуск вечного цикла
    print("Выберите программу: ")
    print('1. Угадай число')
    print('2. Викторина')
    print('3. Баланс')
    print('4. Выход')
    ans = input('Введите номер программы: ')  # ввод и проверка ввода пользователя
    while ans.strip() not in ['1', '2', '3', '4']:
        ans = input('Введите номер программы: ')
    if ans == '1':  # если пользователь ввел 1, то запускаем угадай номер
        number()
    elif ans == '2':  # если 2 - то викторину
        viktorina()
    elif ans == '3':  # если 3 - то баланс
        account()
    else:  # иначе выходим из программы
        break