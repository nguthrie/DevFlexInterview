from question2 import center_zeros


def test_1():
    assert center_zeros([0, 3, 1]) == [3, 0, 1]


def test_2():
    assert center_zeros([1, 1, 3, 0]) == [1, 1, 0, 3]


def test_3():
    assert center_zeros([1, 1, 3, 0, 6, 0]) == [1, 1, 0, 0, 3, 6]


def test_4():
    assert center_zeros([0, 0, 1]) == [0, 0, 1]


def test_5():
    assert center_zeros([]) == []
