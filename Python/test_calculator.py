import calculator3
def test_add():
    calculator3.add(2,3)==5
def test_subtract():
    calculator3.subtract(5,3)==2
def test_multiply():
    calculator3.multiplication(2,3)==6

def test_division():
    calculator3.division(6,2)==3
    calculator3.division(3,0)=='Error'