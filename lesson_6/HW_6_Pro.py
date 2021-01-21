from lesson_5.divisor_master import prime_def

#print((prime_def(10)))

def test_prime_dev():
    assert prime_def(10) == 5

def test_prime_dev1():
    assert prime_def(10) == 7

def test_prime_dev2():
    assert prime_def('ghjk') == 5

test_prime_dev()
#test_prime_dev1()
test_prime_dev2()