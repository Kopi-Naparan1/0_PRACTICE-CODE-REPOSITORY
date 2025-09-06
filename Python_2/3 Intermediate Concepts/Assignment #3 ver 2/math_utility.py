

def add(*args):
    return sum(args)

def sub(x , y):
    result = x - y
    return result

def mul(*args):
    from functools import reduce
    result = reduce(lambda x, y: x * y, args)
    return result

def div(x, y):
    try:
        result = x / y
        return result

    except ValueError:
        return print('ERROR - CAN NOT DIVIDE BY ZERO')