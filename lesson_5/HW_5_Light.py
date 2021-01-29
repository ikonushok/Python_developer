from divisor_master import dividers_num, prime_simple, prime_def

num = int(input('Введите число: '))
print('Проверка числа на простоту: ')
print(prime_simple(num))
print('Список всех делителей числа', num, ': ', dividers_num(num))
print('Cамый большой простой делитель числа', num, ': ', prime_def(num))
