from lesson_5.divisor_master import prime_def, prime_simple, dividers_num
# импортировали методы 5го урока

#print((dividers_num(6)))

def test_diveders_num():
    assert dividers_num(7) == [1, 2, 3, 6]

def test_diveders_num1():
    assert dividers_num(6) == [1, 2, 3, 6]

def test_diveders_num2():
    assert dividers_num('dfg') == [1, 2, 3, 6]

#test_diveders_num()
#test_diveders_num1()
#test_diveders_num2()

def test_prime_simple():
    assert prime_simple(7) == 'Число простое'

def test_prime_simple1():
    assert prime_simple(6) == 'Число простое'

test_prime_simple()
test_prime_simple1()
