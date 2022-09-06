
from cloudpayments.processors import ChargeProcessor

from cloudpayments.enum import Currency, Localization


class CloudPayment:
    """
    Class-facade for describing client methods to interact with cloudpayments.
    Add new method with processor to interact by cloudpayments API.
    """

    @classmethod
    def charge(
            cls, amount: float, ip_address: str, card_cryptogram_packet: str, currency: Currency = Currency.RUB,
            cardholder_name: str = None, payment_url: str = None, invoice_id: str = None, description: str = None,
            culture_name: Localization = Localization.RU, account_id: str = None, email: str = None, payer: dict = None,
            transaction_data: dict = None, require_confirmation: bool = False,
            *args, **kwargs):
        """
        Call charge API method of cloudpayments.
        https://developers.cloudpayments.ru/#vyplata-po-kriptogramme
        """
        return ChargeProcessor(*args, **kwargs).process()
