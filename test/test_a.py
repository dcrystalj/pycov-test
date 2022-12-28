import src.a as a


def test_covered():
    assert a.greet(6) is True
    assert a.greet(7) is True
    assert a.greet(8) is True
