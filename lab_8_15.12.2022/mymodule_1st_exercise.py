def triangle(a, h):
    s = a * h
    s1 = s
    return s1


def square(a):
    s = a**2
    return s


def rectangle(a, b):
    s = a * b
    return s


def rhomb(a, h):
    s = a * h
    return s


def traphezoid(a, b, h):
    s = ((a + b) * h) / 2
    return s


class NumberZero(Exception):
    pass


class NegativeNumber(Exception):
    pass