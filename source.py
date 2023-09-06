def performSub(x, y):
    return x - y 

def performAdd(x, y): 
    return x + y 

def performMult(x, y):
    return x * y

def performDiv(x, y):
    try : div = x / y
    except ZeroDivisionError:
        return "Error: Division by zero"
    return div