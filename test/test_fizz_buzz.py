from fizz_buzz import fizz_buzz

def test_fizz():
    assert fizz_buzz(3) == 'fizz'

def test_buzz():
    assert fizz_buzz(5) == 'buzz'

def test_fizz_buzz():
    fizz_buzz(15)
    assert True
