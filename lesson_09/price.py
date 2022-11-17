from pathlib import Path

from exchange_service import ExchangeRatesService


class Price:
    def __init__(self, amount: int, currency: str) -> None:
        self.amount: int = amount
        self.currency: str = currency.lower()

    def __add__(self, other: "Price"):
        if self.currency != other.currency:
            return self.amount + es.converter(
                other.currency, self.currency, other.amount
            )
        else:
            return self.amount + other.amount

    def __sub__(self, other: "Price"):
        if self.currency != other.currency:
            return self.amount - es.converter(
                other.currency, self.currency, other.amount
            )
        else:
            return self.amount - other.amount


FILENAME = Path(__file__).parent / "exchange_rates.json"
es = ExchangeRatesService(FILENAME)

a = Price(100, "USD")
b = Price(50, "EUR")
d = Price(20, "USD")
c = Price(200, "UAh")

assert a + d == 100 + 20
assert b + d == 50 + 20 * 0.97
assert d + b == 20 + 50 * 1.03
assert a + c == 100 + 200 * 0.027
assert c + a == 200 + 100 * 36.95
assert b + c == 50 + 200 * 0.027 * 0.97
assert c + b == 200 + 50 * 1.03 * 36.95
