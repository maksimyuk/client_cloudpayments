
from cloudpayments.processors import ChargeProcessor

from cloudpayments.enum import Currency, Localization
from cloudpayments.models import ChargeRequestSchema


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
            json_data: dict = None, require_confirmation: bool = False,
            *args, **kwargs):
        """
        Call charge API method of cloudpayments.
        https://developers.cloudpayments.ru/#vyplata-po-kriptogramme
        """
        # deserialize incoming params into dict
        # TODO предполагаю, что по-хорошему нужно было бы описывать дата-класс, в который входящие аргументы функции
        #  будут маппиться
        charge_params = ChargeRequestSchema().load({
            'Amount': amount,
            'IpAddress': ip_address,
            'CardCryptogramPacket': card_cryptogram_packet,
            'Currency': currency.name,
            'Name': cardholder_name,
            'PaymentUrl': payment_url,
            'InvoiceId': invoice_id,
            'Description': description,
            'CultureName': culture_name.name,
            'AccountId': account_id,
            'Email': email,
            'Payer': payer,
            'JsonData': json_data,
        })

        return ChargeProcessor().process(schema=charge_params, require_confirmation=require_confirmation)
