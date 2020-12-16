from divisor_master import dividers_num

num = int(input('Введите число: '))

def list_simple_dividers(num):
    prime_list = dividers_num(num)[1:]
    print(prime_list)
    result = []

    for i in prime_list:
        while num % i == 0:
            result.append(i)
            num //= i
        if num == 1:
            break
    return result

print('Каноническое разложение числа: ', list_simple_dividers(num))

def divider_max(num):
    return max(dividers_num(num)[:-2])

print('Самый большой делитель: ', divider_max(num) )