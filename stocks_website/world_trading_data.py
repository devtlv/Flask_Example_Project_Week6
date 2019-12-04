from urllib.parse import urljoin

import dataclasses

import typing
from flask import current_app as app
import requests


@dataclasses.dataclass
class WTDRepository:
    api_token: str = None
    base_url: str = 'https://api.worldtradingdata.com/api/v1/'
    session: requests.Session = requests.Session()

    def __post_init__(self):
        if not self.api_token:
            if not app.config.world_trading_data_api_token:
                raise ValueError("Need an API key.")
            self.api_token = app.config.world_trading_data_api_token

    def _get(self, endpoint: str, **kwargs) -> requests.Response:
        url = urljoin(self.base_url, endpoint)
        response = self.session.get(url, params={'api_token': self.api_token, **kwargs})
        response.raise_for_status()
        return response

    def get(self, endpoint: str, **kwargs) -> typing.Any:
        response = self._get(endpoint, **kwargs)

        return response.json()
