
from abc import abstractmethod


class BaseMethodProcessor:
    """
    Class for setting interface for CloudPayment method processor.
    You need inherit this class to add new method processor.
    """

    @classmethod
    @abstractmethod
    async def process(cls, *args, **kwargs):
        pass
