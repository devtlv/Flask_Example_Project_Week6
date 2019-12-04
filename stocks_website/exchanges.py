from __future__ import annotations

import dataclasses
import typing

import pytz

from stocks_website.world_trading_data import WTDRepository


@dataclasses.dataclass()
class StockExchange:
    name: str
    symbol: str
    timezone: str

    def __post_init__(self):
        if not self.symbol:
            raise ValueError("Symbol cannot be empty.")

        if not self.name:
            self.name = self.symbol

        if not self.timezone:
            raise ValueError("Timezone name cannot be empty.")

        self.timezone = pytz.timezone(self.timezone)
        self.symbol = self.symbol.upper()

    @staticmethod
    def create_from_wdt(symbol: str,
                        stock_exchange_long: str = None,
                        timezone_name: str = None) -> StockExchange:
        """Create a stock exchange instance
        from the worldtradingdata.com API.

        A factory method which creates a stock exchange from a response
        to a request from `api/v1/exchange_list`.

        :param symbol: The stock exchange's symbol.
        :param stock_exchange_long: The stock exchange's full name.
        :param timezone_name: The stock exchange's timezone in a string representation.

        :raises ValueError: When one of the arguments is empty a value error is raised.
        :raises pytz.TimezoneError: When the string representation of the timezone isn't valid
        :returns: A new :class:`StockExchange` object.
        """
        return StockExchange(
            symbol=symbol,
            name=stock_exchange_long,
            timezone=timezone_name
        )


class StockExchangesRepository(WTDRepository):
    def get_stock_exchanges(self) -> typing.List[StockExchange]:
        stock_exchanges = self.get('exchange_list')

        if 'message' in stock_exchanges:
            raise ValueError(stock_exchanges['message'])
        return [
            StockExchange.create_from_wdt(symbol, **data) for symbol, data in stock_exchanges.items()
        ]
