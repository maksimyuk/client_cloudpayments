
from typing import Any, Dict

from aiohttp.connector import TCPConnector

from cloudpayments.base.client import AbstractInteractionClient
from cloudpayments.interaction.decorators import basic_auth, idempotence


class CloudPaymentInteractionClient(AbstractInteractionClient):
    """Client for interacting with cloudpayments API."""

    SERVICE = 'cloudpayments'
    BASE_URL = 'https://api.cloudpayments.ru'

    def __init__(self):
        super().__init__()
        # Иначе ошибка в тестах Event loop is closed.
        self.CONNECTOR = TCPConnector(limit=30)

    @basic_auth
    @idempotence
    def _get_session_kwargs(self) -> Dict[str, Any]:
        return super()._get_session_kwargs()

