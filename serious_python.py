import pytest


class Car(object):
    def __init__(self, name):
        self.name = name


c1 = Car("Tesla")


@pytest.fixture
def car():
    return Car("Tesla")


def test_car_name(car):
    assert car.name == "Tesla"


def test_car_name2(car):
    assert car.name == "esla"

    # def test_true():
    #     assert True

    # @pytest.mark.skipif(2 == 1, reason="skip this test")
    # def test_false():
    #     assert False
