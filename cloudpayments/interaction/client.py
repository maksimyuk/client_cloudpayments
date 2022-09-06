
from typing import Any, Dict

from aiohttp.connector import TCPConnector

from cloudpayments.base.client import AbstractInteractionClient
from cloudpayments.interaction.decorators import basic_auth, idempotence


class CloudPaymentInteractionClient(AbstractInteractionClient):
    """Client for interacting with cloudpayments API."""

    CONNECTOR = TCPConnector(limit=25, limit_per_host=5)
    SERVICE = 'test'
    BASE_URL = 'test'

    @basic_auth
    @idempotence
    def _get_session_kwargs(self) -> Dict[str, Any]:
        return super()._get_session_kwargs()

