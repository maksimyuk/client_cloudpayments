
from cloudpayments.base.processors import BaseMethodProcessor


class ChargeProcessor(BaseMethodProcessor):
    """
    Class for processing charge method request.
    https://developers.cloudpayments.ru/#oplata-po-kriptogramme
    """

    def process(self):
        """Process payment by cryptogram."""
