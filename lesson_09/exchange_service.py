import json
from pathlib import Path


class ExchangeRate:
    def __init__(self, from_: str, to_: str, value: float) -> None:
        self.from_: str = from_
        self.to_: str = to_
        self.value: float = value

    def __repr__(self) -> str:
        return f"{self.from_}-{self.to_}: {self.value}"


class ExchangeRatesService:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            return cls._instance
        cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, filename: Path) -> None:
        if self._initialized:
            return

        self.filename: Path = filename
        self.rates: list[ExchangeRate] = self._get_rates()

        self._initialized = True

    def _get_rates(self) -> list[ExchangeRate]:
        with open(self.filename) as file:
            print("READING FROM FILE...")
            raw_data: str = file.read()
            data: dict = json.loads(raw_data)

        return [
            ExchangeRate(
                from_=element["from_"],
                to_=element["to_"],
                value=element["value"],
            )
            for element in data["results"]
        ]

    def converter(self, currency_from: str, currency_to: str, value):
        for i in self.rates:
            if i.from_ == currency_from and i.to_ == currency_to:
                return i.value * value
        for i in self.rates:
            if i.from_ == currency_from and i.to_ == "usd":
                return self.converter(i.to_, currency_to, i.value * value)
