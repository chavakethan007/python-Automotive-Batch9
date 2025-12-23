def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    if y==0:
        return ZeroDivisionError
    else:
        return x/y
    
def power(x,y):
    return x**y