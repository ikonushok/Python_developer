from math import pi, sqrt, pow, hypot
# имтортировали методы

def test_pi():
    assert pi == 3.1415926
#test_pi()

def test_pi1():
    assert pi == 'yes'
#test_pi1()

def test_sqrt():
    assert sqrt(9) == 3
#test_sqrt()

def test_sqrt1():
    assert sqrt(9) == 2
#test_sqrt1()

def test_pow():
    assert pow(2, 3) == 8
#test_pow()

def test_pow1():
    assert pow(2, 3) == 9
#test_pow1()

def test_hypot():
    assert hypot(3, 4) == 5
#test_hypot()

def test_hypot1():
    assert hypot(3, 4) == 5.3
test_hypot1()