
import pytest

from cloudpayments.models import ChargeRequestSchema, Secure3dAuthenticationSchema, TransactionSchema


@pytest.fixture()
def charge_request_serialized(raw_charge_request) -> ChargeRequestSchema:
    """Serialized example of ChargeRequestSchema."""
    return ChargeRequestSchema().load(raw_charge_request)


@pytest.fixture()
def secure_3d_authentication_serialized(raw_secure_3d_response) -> Secure3dAuthenticationSchema:
    """Serialized example of Secure3dAuthenticationSchema."""
    return Secure3dAuthenticationSchema().load(raw_secure_3d_response)


@pytest.fixture()
def transaction_serialized(raw_transaction_response) -> TransactionSchema:
    """Serialized example of TransactionSchema."""
    return TransactionSchema().load(raw_transaction_response)


@pytest.fixture()
def charge_response_success() -> dict:
    """Example of success response."""
    return {
        'Model': {
            'ReasonCode': 0,
            'PublicId': 'pk_********************************',
            'TerminalUrl': 'http://test.test',
            'TransactionId': 891510444,
            'Amount': 10,
            'Currency': 'RUB',
            'CurrencyCode': 0,
            'PaymentAmount': 10,
            'PaymentCurrency': 'RUB',
            'PaymentCurrencyCode': 0,
            'InvoiceId': '1234567',
            'AccountId': 'user_x',
            'Email': None,
            'Description': 'Оплата товаров в example.com',
            'JsonData': None,
            'CreatedDate': '/Date(1635150224630)/',
            'PayoutDate': None,
            'PayoutDateIso': None,
            'PayoutAmount': None,
            'CreatedDateIso': '2021-10-25T08:23:44',
            'AuthDate': '/Date(1635150224739)/',
            'AuthDateIso': '2021-10-25T08:23:44',
            'ConfirmDate': None,
            'ConfirmDateIso': None,
            'AuthCode': 'A1B2C3',
            'TestMode': True,
            'Rrn': None,
            'OriginalTransactionId': None,
            'FallBackScenarioDeclinedTransactionId': None,
            'IpAddress': '123.123.123.123',
            'IpCountry': 'CN',
            'IpCity': 'Beijing',
            'IpRegion': 'Beijing',
            'IpDistrict': 'Beijing',
            'IpLatitude': 39.9289,
            'IpLongitude': 116.3883,
            'CardFirstSix': '411111',
            'CardLastFour': '1111',
            'CardExpDate': '11/25',
            'CardType': 'Visa',
            'CardProduct': 'C',
            'CardCategory': 'Visa Signature (Signature)',
            'EscrowAccumulationId': None,
            'IssuerBankCountry': 'RU',
            'Issuer': 'CloudPayments',
            'CardTypeCode': 0,
            'Status': 'Authorized',
            'StatusCode': 2,
            'CultureName': 'ru',
            'Reason': 'Approved',
            'CardHolderMessage': 'Оплата успешно проведена',
            'Type': 0,
            'Refunded': False,
            'Name': 'CARDHOLDER NAME',
            'Token': '0a0afb77-8f41-4de2-9524-1057f9695303',
            'SubscriptionId': None,
            'GatewayName': 'Test',
            'ApplePay': False,
            'AndroidPay': False,
            'WalletType': '',
            'TotalFee': 0
        },
        'Success': True,
        'Message': None
    }


@pytest.fixture()
def charge_response_incorrect_request() -> dict:
    """Example of response for incorrect answer."""
    return {
        'Success': False,
        'Message': 'Amount is required'
    }


@pytest.fixture()
def charge_response_charge_declined() -> dict:
    """Example of response for declined charge."""
    return {
        'Model': {
            'ReasonCode': 5051,
            'PublicId': 'pk_**********************************',
            'TerminalUrl': 'http://test.test',
            'TransactionId': 891583633,
            'Amount': 10,
            'Currency': 'RUB',
            'CurrencyCode': 0,
            'PaymentAmount': 10,
            'PaymentCurrency': 'RUB',
            'PaymentCurrencyCode': 0,
            'InvoiceId': '1234567',
            'AccountId': 'user_x',
            'Email': None,
            'Description': 'Оплата товаров в example.com',
            'JsonData': None,
            'CreatedDate': '/Date(1635154784619)/',
            'PayoutDate': None,
            'PayoutDateIso': None,
            'PayoutAmount': None,
            'CreatedDateIso': '2021-10-25T09:39:44',
            'AuthDate': None,
            'AuthDateIso': None,
            'ConfirmDate': None,
            'ConfirmDateIso': None,
            'AuthCode': None,
            'TestMode': True,
            'Rrn': None,
            'OriginalTransactionId': None,
            'FallBackScenarioDeclinedTransactionId': None,
            'IpAddress': '123.123.123.123',
            'IpCountry': 'CN',
            'IpCity': 'Beijing',
            'IpRegion': 'Beijing',
            'IpDistrict': 'Beijing',
            'IpLatitude': 39.9289,
            'IpLongitude': 116.3883,
            'CardFirstSix': '400005',
            'CardLastFour': '5556',
            'CardExpDate': '12/25',
            'CardType': 'Visa',
            'CardProduct': None,
            'CardCategory': None,
            'EscrowAccumulationId': None,
            'IssuerBankCountry': 'US',
            'Issuer': 'ITS Bank',
            'CardTypeCode': 0,
            'Status': 'Declined',
            'StatusCode': 5,
            'CultureName': 'ru',
            'Reason': 'InsufficientFunds',
            'CardHolderMessage': 'Недостаточно средств на карте',
            'Type': 0,
            'Refunded': False,
            'Name': 'CARDHOLDER NAME',
            'Token': 'tk_255c42192323f2e09ea17635302c3',
            'SubscriptionId': None,
            'GatewayName': 'Test',
            'ApplePay': False,
            'AndroidPay': False,
            'WalletType': '',
            'TotalFee': 0
        },
        'Success': False,
        'Message': None
    }


@pytest.fixture()
def charge_response_secure_3d() -> dict:
    """Example of response for secure 3d."""
    return {
        "Model": {
            "TransactionId": 891463508,
            "PaReq": "+/eyJNZXJjaGFudE5hbWUiOm51bGwsIkZpcnN0U2l4IjoiNDI0MjQyIiwiTGFzdEZvdXIiOiI0MjQyIiwiQW1vdW50IjoxMDAuMCwiQ3VycmVuY3lDb2RlIjoiUlVCIiwiRGF0ZSI6IjIwMjEtMTAtMjVUMDA6MDA6MDArMDM6MDAiLCJDdXN0b21lck5hbWUiOm51bGwsIkN1bHR1cmVOYW1lIjoicnUtUlUifQ==",
            "GoReq": None,
            "AcsUrl": "https://demo.cloudpayments.ru/acs",
            "ThreeDsSessionData": None,
            "IFrameIsAllowed": True,
            "FrameWidth": None,
            "FrameHeight": None,
            "ThreeDsCallbackId": "7be4d37f0a434c0a8a7fc0e328368d7d",
            "EscrowAccumulationId": None
        },
        "Success": False,
        "Message": None
    }
