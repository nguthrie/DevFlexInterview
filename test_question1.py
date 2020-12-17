from question1 import select_max


def test_1():
    assert select_max([1, 2, 3]) == 3


def test_2():
    assert select_max([0]) == 0


def test_3():
    assert select_max([0, 0, 0]) == 0


def test_4():
    assert select_max([-10, -2, -8]) == -2


def test_5():
    assert select_max([-10, -2, 1]) == 1


def test_6():
    assert select_max([]) == None



