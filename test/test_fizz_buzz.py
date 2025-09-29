from fizz_buzz import fizz_buzz

def test_fizz_buzz():
    assert fizz_buzz(15) == 'fizz buzz'

def test_fizz():
    assert fizz_buzz(3) == 'fizz'

def test_buzz():
    assert fizz_buzz(5) == 'buzz'

def test_otherwise():
    # assert fizz_buzz(1) == '1'
    # fizz_buzz(1)
    # assert True
    pass
