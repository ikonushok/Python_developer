def number():
    a = print("Загадайте число от 0 до 100")
    start = 0
    end = 100
    for i in range(start, end + 1):
        if (end - start) > 2:
            m = (start + end) // 2
            print('Ваше число больше', m, ' ?')
            s = input('да или нет:')
            if s == 'да':
                start = m
            else:
                end = m
        else:
            break

    for i in range(start, end + 1):
        print('Ваше число равно', i, ' ?')
        s = input('да или нет:')
        if s == 'да':
            print('Я угадал !!!')
            break