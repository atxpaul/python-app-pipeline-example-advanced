import pytest
from app import GeometryCalculator

@pytest.fixture
def calculator():
    return GeometryCalculator()

def test_area_of_rectangle(calculator):
    assert calculator.area_of_rectangle(3, 4) == 12
    with pytest.raises(ValueError):
        calculator.area_of_rectangle(-1, 4)

def test_perimeter_of_rectangle(calculator):
    assert calculator.perimeter_of_rectangle(3, 4) == 14
    with pytest.raises(ValueError):
        calculator.perimeter_of_rectangle(0, 4)

def test_area_of_circle(calculator):
    assert pytest.approx(calculator.area_of_circle(5), 0.0001) == 78.53975
    with pytest.raises(ValueError):
        calculator.area_of_circle(-5)

def test_perimeter_of_circle(calculator):
    assert pytest.approx(calculator.perimeter_of_circle(5), 0.0001) == 31.4159
    with pytest.raises(ValueError):
        calculator.perimeter_of_circle(0)