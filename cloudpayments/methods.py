
from cloudpayments.processors import ChargeProcessor


class CloudPayment:
    """
    Class-facade for describing client methods to interact with cloudpayments.
    Add new method with processor to interact by cloudpayments API.
    """

    @classmethod
    def charge(cls, *args, **kwargs):
        """Call charge API method of cloudpayments."""
        return ChargeProcessor(*args, **kwargs).process()