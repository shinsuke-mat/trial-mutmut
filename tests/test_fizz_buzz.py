from fizz_buzz import X

def test_fizz_buzz():
    assert X.fizz_buzz(15) == 'fizz buzz'

def test_fizz():
    assert X.fizz_buzz(3) == 'fizz'

def test_buzz():
    assert X.fizz_buzz(5) == 'buzz'

def test_otherwise():
    assert X.fizz_buzz(1) == '1'
    X.fizz_buzz(1)
    assert True
    pass
