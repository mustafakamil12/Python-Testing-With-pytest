import pytest
import math

def square(name):
    def decorator(func):
        setattr(func, 'square', name)
        return func
    return decorator


def others(name):
    def decorator(func):
        setattr(func, 'others', name)
        return func
    return decorator

@square('sqrt')
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

@square('square')
def testsquare():
    num = 7
    assert 7 * 7 == 40

@others('equality')
def testequality():
    assert 10 == 11