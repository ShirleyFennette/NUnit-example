from decimal import Decimal


def total(prices, discount=0):
    if not 0 <= discount <= 100:
        raise ValueError("Discount must be between 0 and 100")
    return (sum((Decimal(str(p)) for p in prices), Decimal("0"))
            * (Decimal("1") - Decimal(str(discount)) / 100)).quantize(Decimal("0.01"))
