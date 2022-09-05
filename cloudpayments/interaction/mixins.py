
from typing import Any, Dict
from uuid import uuid4

from aiohttp import BasicAuth


class BasicAuthorizationMixin:
    """Auth-mixin for client session."""

    def _get_session_kwargs(self) -> Dict[str, Any]:
        # TODO возможно нужно переопределять не просто метод _get_session_kwargs, а create_session,
        #  т.к. метод _get_session_kwargs - приватный
        """
        Updates session kwargs necessary for creating a session instance by auth data.
        https://developers.cloudpayments.ru/#autentifikatsiya-zaprosov
        """
        session_kwargs = super()._get_session_kwargs()
        session_kwargs.update({
            'auth': BasicAuth(login='test', password='test')
        })

        return session_kwargs


class IdempotenceMixin:
    """Mixin for adding unique id in header such as X-Request-ID."""

    @staticmethod
    def _generate_request_id() -> str:
        """Returns unique request id."""
        return str(uuid4())

    def _get_session_kwargs(self) -> Dict[str, Any]:
        """
        Updates session kwargs for adding special header X-Request-ID.
        https://developers.cloudpayments.ru/#idempotentnost-api
        """
        headers = {
            'X-Request-ID': self._generate_request_id(),
        }

        session_kwargs = super()._get_session_kwargs()
        session_kwargs.update(headers)

        return session_kwargs
