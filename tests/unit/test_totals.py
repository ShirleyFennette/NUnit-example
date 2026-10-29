from decimal import Decimal
import allure
import pytest
from app import total


@allure.suite("Unit")
@pytest.mark.parametrize("prices,discount,expected", [
    ([], 0, "0.00"), ([10, 20], 0, "30.00"),
    ([10, 20], 10, "27.00"), ([0.1, 0.2], 0, "0.30"),
])
def test_total(prices, discount, expected):
    assert total(prices, discount) == Decimal(expected)


@allure.suite("Unit")
def test_invalid_discount():
    with pytest.raises(ValueError):
        total([10], 101)
