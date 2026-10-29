from decimal import Decimal
import json
import allure
from app import total


@allure.suite("Functional")
def test_checkout_with_discount():
    with allure.step("Add two products to the cart"):
        cart = [{"sku": "book", "price": 20}, {"sku": "pen", "price": 5}]
        allure.attach(json.dumps(cart), "cart", allure.attachment_type.JSON)
    with allure.step("Apply a 20 percent discount"):
        amount = total([item["price"] for item in cart], 20)
    with allure.step("Verify payable amount"):
        assert amount == Decimal("20.00")


@allure.suite("Functional")
def test_remove_product():
    cart = [20, 5]
    with allure.step("Remove the last product"):
        cart.pop()
    assert total(cart) == Decimal("20.00")
