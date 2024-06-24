import pytest

def great(name):
    def decorator(func):
        setattr(func, 'great', name)
        return func
    return decorator


def others(name):
    def decorator(func):
        setattr(func, 'others', name)
        return func
    return decorator

@pytest.mark.greate
def test_greater():
    num = 100
    assert num > 100

@pytest.mark.greate
def test_greater_equal():
    num = 100
    assert num >= 100

@pytest.mark.others
def test_less():
    num = 100
    assert num < 100