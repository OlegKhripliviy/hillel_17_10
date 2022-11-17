from dataclasses import dataclass
from pathlib import Path

from exchange_service import ExchangeRatesService


@dataclass
class Price:
    amount: int
    currency: str

    def __add__(self, other: "Price"):
        if self.currency.lower() != other.currency.lower():
            return self.amount + es.converter(
                other.currency.lower(), self.currency.lower(), other.amount
            )
        else:
            return self.amount + other.amount

    def __sub__(self, other: "Price"):
        if self.currency.lower() != other.currency.lower():
            return self.amount - es.converter(
                other.currency.lower(), self.currency.lower(), other.amount
            )
        else:
            return self.amount - other.amount


FILENAME = Path(__file__).parent / "exchange_rates.json"
es = ExchangeRatesService(FILENAME)
