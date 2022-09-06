
from cloudpayments.processors import ChargeProcessor


class CloudPayment:

    @classmethod
    def charge(cls, *args, **kwargs):
        return ChargeProcessor(*args, **kwargs).process()