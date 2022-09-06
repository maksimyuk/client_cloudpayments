
from abc import abstractmethod


class BaseMethodProcessor:
    """
    Class for setting interface for CloudPayment method processor.
    You need inherit this class to add new method processor.
    """

    def __init__(self, *args, **kwargs):
        pass

    async def process(self, *args, **kwargs):
        pass
