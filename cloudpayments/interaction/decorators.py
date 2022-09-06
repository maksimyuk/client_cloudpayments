
from typing import Any, Callable, Dict
from uuid import uuid4

from aiohttp import BasicAuth


def basic_auth(func: Callable) -> Callable:
    """
    Decorator for auth for client session.
    https://developers.cloudpayments.ru/#autentifikatsiya-zaprosov
    """
    def wrapper(*args, **kwargs) -> Dict:
        session_kwargs = func(*args, **kwargs)
        session_kwargs.update({
            'auth': BasicAuth(login='test', password='test')
        })

        return session_kwargs

    return wrapper


def idempotence(func: Callable) -> Callable:
    """
    Decorator for adding unique id in header such as X-Request-ID.
    https://developers.cloudpayments.ru/#idempotentnost-api
    """
    def wrapper(*args, **kwargs) -> Dict:
        session_kwargs = func(*args, **kwargs)

        headers = {
            'X-Request-ID': str(uuid4()),
        }
        session_kwargs.update({'headers': headers})

        return session_kwargs

    return wrapper
