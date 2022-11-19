from dataclasses import dataclass
from pathlib import Path

from exchange_service import ExchangeRatesService


@dataclass
class Price:
    amount: int or float
    currency: str

    def __add__(self, other: "Price") -> "Price":
        if self.currency.lower() != other.currency.lower():
            amount_after_convert = self.amount + es.converter(
                other.currency.lower(), self.currency.lower(), other.amount
            )
            return Price(amount_after_convert, self.currency)
        else:
            return Price(self.amount + other.amount, self.currency)

    def __sub__(self, other: "Price") -> "Price":
        if self.currency.lower() != other.currency.lower():
            amount_after_convert = self.amount - es.converter(
                other.currency.lower(), self.currency.lower(), other.amount
            )
            return Price(amount_after_convert, self.currency)
        else:
            return Price(self.amount - other.amount, self.currency)


FILENAME = Path(__file__).parent / "exchange_rates.json"
es = ExchangeRatesService(FILENAME)

a = Price(100, "USD")
b = Price(50, "EUR")
d = Price(20, "USD")
c = Price(200, "UAh")

assert a + d == Price(100 + 20, a.currency)
assert b + d == Price(50 + 20 * 0.97, b.currency)
assert d + b == Price(20 + 50 * 1.03, d.currency)
assert a + c == Price(100 + 200 * 0.027, a.currency)
assert c + a == Price(200 + 100 * 36.95, c.currency)
assert b + c == Price(50 + 200 * 0.027 * 0.97, b.currency)
assert c + b == Price(200 + 50 * 1.03 * 36.95, c.currency)
assert a - d == Price(100 - 20, a.currency)
assert b - d == Price(50 - 20 * 0.97, b.currency)
assert d - b == Price(20 - 50 * 1.03, d.currency)
assert a - c == Price(100 - 200 * 0.027, a.currency)
assert c - a == Price(200 - 100 * 36.95, c.currency)
assert b - c == Price(50 - 200 * 0.027 * 0.97, b.currency)
assert c - b == Price(200 - 50 * 1.03 * 36.95, c.currency)
