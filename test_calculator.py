import calculator

def test_add():
    assert calculator.add(2, 3) == 5

def test_subtract():
    assert calculator.subtract(10, 4) == 6

def test_multiply():
    assert calculator.multiply(3, 7) == 21

def test_divide():
    assert calculator.divide(12, 3) == 4
