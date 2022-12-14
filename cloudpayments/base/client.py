import asyncio
import random
import time
from itertools import chain
from typing import ClassVar, Optional, Type, Dict, Any

from aiohttp import TCPConnector, ClientSession, ClientTimeout, ClientResponse

from cloudpayments.base.error import InteractionResponseError


class AbstractInteractionClient:
    CONNECTOR: ClassVar[TCPConnector]

    REQUEST_TIMEOUT: ClassVar[Optional[float]] = None
    CONNECT_TIMEOUT: ClassVar[Optional[float]] = None

    SERVICE: ClassVar[str]
    BASE_URL: ClassVar[str]
    REQUEST_RETRY_TIMEOUTS = (0.1, 0.2, 0.4)

    _session: Optional[ClientSession] = None

    def __init__(self) -> None:
        self.default_timeout: Optional[ClientTimeout] = None
        if self.REQUEST_TIMEOUT:
            self.default_timeout = ClientTimeout(total=self.REQUEST_TIMEOUT, connect=self.CONNECT_TIMEOUT)

    def _get_session_cls(self) -> Type[ClientSession]:
        return ClientSession

    def _get_session_kwargs(self) -> Dict[str, Any]:
        """Returns kwargs necessary for creating a session instance."""
        kwargs = {
            'connector': self.CONNECTOR,
            'connector_owner': False,
            'trust_env': True,
        }
        if self.default_timeout:
            kwargs['timeout'] = self.default_timeout
        return kwargs

    @property
    def session(self) -> ClientSession:
        if self._session is None:
            self._session = self.create_session()
        return self._session

    def create_session(self) -> ClientSession:
        session_cls = self._get_session_cls()
        kwargs = self._get_session_kwargs()
        return session_cls(**kwargs)

    async def _handle_response_error(self, response: ClientResponse) -> None:
        raise InteractionResponseError(
            status_code=response.status,
            method=response.method,
            service=self.SERVICE,
            params=None,
        )

    async def _process_response(self, response: ClientResponse, interaction_method: str) -> Dict[str, Any]:
        if response.status >= 400:
            await self._handle_response_error(response)
        return await response.json()

    async def _make_request(
        self,
        interaction_method: str,
        method: str,
        url: str,
        **kwargs: Any
    ) -> ClientResponse:
        """Wraps ClientSession.request allowing retries, updating metrics."""

        kwargs.setdefault('headers', {})

        response_time = 0.0
        response = exc = None
        for retry_number, retry_delay in enumerate(chain((0.0,), self.REQUEST_RETRY_TIMEOUTS)):
            if retry_delay:
                delay = retry_delay - response_time
                await asyncio.sleep(delay + random.uniform(-delay / 2, delay / 2))

            exc = None
            response = None
            before = time.monotonic()
            try:
                response = await self.session.request(method, url, **kwargs)

                assert response is not None
                success = True
            except Exception as e:
                exc = e
                success = False

            response_time = time.monotonic() - before

            if success or isinstance(exc, asyncio.TimeoutError):
                break

        if exc:
            raise exc

        return response  # type: ignore

    async def _request(  # noqa: C901
        self,
        interaction_method: str,
        method: str,
        url: str,
        **kwargs: Any,
    ) -> Dict[str, Any]:

        response = await self._make_request(interaction_method, method, url, **kwargs)
        processed = await self._process_response(response, interaction_method)

        return processed

    async def get(self, interaction_method: str, url: str, **kwargs: Any) -> Dict[str, Any]:
        return await self._request(interaction_method, 'GET', url, **kwargs)

    async def post(self, interaction_method: str, url: str, **kwargs: Any) -> Dict[str, Any]:
        return await self._request(interaction_method, 'POST', url, **kwargs)

    async def put(self, interaction_method: str, url: str, **kwargs: Any) -> Dict[str, Any]:
        return await self._request(interaction_method, 'PUT', url, **kwargs)

    async def patch(self, interaction_method: str, url: str, **kwargs: Any) -> Dict[str, Any]:
        return await self._request(interaction_method, 'PATCH', url, **kwargs)

    async def delete(self, interaction_method: str, url: str, **kwargs: Any) -> Dict[str, Any]:
        return await self._request(interaction_method, 'DELETE', url, **kwargs)

    async def close(self) -> None:
        if self._session:
            await self._session.close()
            self._session = None

    def endpoint_url(self, relative_url: str, base_url_override: Optional[str] = None) -> str:
        base_url = (base_url_override or self.BASE_URL).rstrip('/')
        relative_url = relative_url.lstrip('/')
        return f'{base_url}/{relative_url}'
