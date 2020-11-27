print('Hello')
print('Hello', 'World', '!!!')
print('Hello', 'World', '!!!', sep=' ===> ')
print('Hello', 'World', '!!!', sep=' ===> ', end=' The Show must go on!')
print('\n')

#a = input('Введите число: ')
#if a.replace('.', '', 1).isdigit():
#    a = float(a)
#    if a <= 5: print(a, ' меньше или равно 5')
#    elif 5 > a <8: print(a, ' больше 5 и меньше 8')
#    else: print(a, ' больше или равно 8')
#else: print(a, ' не число')

a = 15
while a <= 22:
    print(a, '*', a, '=', a*a)
    a += 1