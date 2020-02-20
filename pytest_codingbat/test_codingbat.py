from main import first_last6, same_first_last, make_pi


def test_first_last6():
    assert first_last6([1, 2, 6]) is True
    assert first_last6([6, 1, 2, 3]) is True
    assert first_last6([13, 6,  1, 2, 3]) is False


def test_same_first_last():
    assert same_first_last([1, 2, 3]) is False
    assert same_first_last([1, 2, 3, 1]) is True
    assert same_first_last([1, 2, 1]) is True


def test_make_pi():
    assert make_pi() == [3, 1, 4]
