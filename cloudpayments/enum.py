
from enum import Enum


class Currency(Enum):
    """
    Partial currency enum.
    https://developers.cloudpayments.ru/#spisok-valyut
    """
    RUB = 'RUB'
    EUR = 'EUR'
    USD = 'USD'


class Localization(Enum):
    """
    Partial localization of notification.
    https://developers.cloudpayments.ru/#lokalizatsiya
    """
    RU = 'ru-RU'
    EN = 'en-US'
