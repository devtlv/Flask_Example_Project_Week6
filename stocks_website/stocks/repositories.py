from __future__ import annotations

import dataclasses
import typing
from enum import Enum

from stocks_website.world_trading_data import WTDRepository


@dataclasses.dataclass
class StockOverview(object):
    symbol: str
    name: str
    currency: str
    price: float
    stock_exchange_name: str
    stock_exchange_symbol: str

    @staticmethod
    def create_from_wtd(symbol: str,
                        name: str,
                        currency: str,
                        price: float,
                        stock_exchange_long: str,
                        stock_exchange_short: str) -> StockOverview:
        return StockOverview(symbol,
                             name,
                             currency,
                             price,
                             stock_exchange_long,
                             stock_exchange_short)


class SearchByOption(Enum):
    symbol = 'symbol'
    name = 'name'
    both = 'symbol,name'


class StocksRepository(WTDRepository):
    def search(self,
               search_term: typing.Union[str, None] = None,
               search_by: typing.Union[SearchByOption, None] = None,
               stock_exchange: typing.Union[typing.List[str], str, None] = None,
               currency: typing.Union[typing.List[str], str, None] = None) -> typing.List[StockOverview]:
        if stock_exchange is None:
            stock_exchange = ()
        if isinstance(stock_exchange, str):
            stock_exchange = (stock_exchange,)

        if currency is None:
            currency = ()
        if isinstance(currency, str):
            currency = (currency,)

        stocks = self.get('stock_search',
                          search_term=search_term,
                          search_by=search_by,
                          stock_exchange=','.join(stock_exchange),
                          currency=','.join(currency))

        if 'message' in stocks and 'data' not in stocks:
            raise ValueError(stocks['message'])

        stocks_data = stocks['data']
        return [
            StockOverview.create_from_wtd(**data) for data in stocks_data
        ]
