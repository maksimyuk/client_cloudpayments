import pytest

from cloudpayments.models import Secure3dAuthenticationSchema, TransactionSchema


@pytest.fixture()
def raw_secure_3d_response() -> dict:
    """Fixture for response with 3-D secure data."""
    return {
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
    }


class TestSecure3dAuthenticationSchema:
    """Test case for checking serialization."""

    def test_serialization(self, raw_secure_3d_response):
        """Check for successful serialization."""
        serialized = Secure3dAuthenticationSchema().load(raw_secure_3d_response)

        assert serialized


@pytest.fixture()
def raw_transaction_response() -> dict:
    """Fixture for response with transaction data."""
    return {
        "ReasonCode": 0,
        "PublicId": "pk_********************************",
        "TerminalUrl": "http://test.test",
        "TransactionId": 891510444,
        "Amount": 10,
        "Currency": "RUB",
        "CurrencyCode": 0,
        "PaymentAmount": 10,
        "PaymentCurrency": "RUB",
        "PaymentCurrencyCode": 0,
        "InvoiceId": "1234567",
        "AccountId": "user_x",
        "Email": None,
        "Description": "Оплата товаров в example.com",
        "JsonData": None,
        "CreatedDate": "/Date(1635150224630)/",
        "PayoutDate": None,
        "PayoutDateIso": None,
        "PayoutAmount": None,
        "CreatedDateIso": "2021-10-25T08:23:44",
        "AuthDate": "/Date(1635150224739)/",
        "AuthDateIso": "2021-10-25T08:23:44",
        "ConfirmDate": None,
        "ConfirmDateIso": None,
        "AuthCode": "A1B2C3",
        "TestMode": True,
        "Rrn": None,
        "OriginalTransactionId": None,
        "FallBackScenarioDeclinedTransactionId": None,
        "IpAddress": "123.123.123.123",
        "IpCountry": "CN",
        "IpCity": "Beijing",
        "IpRegion": "Beijing",
        "IpDistrict": "Beijing",
        "IpLatitude": 39.9289,
        "IpLongitude": 116.3883,
        "CardFirstSix": "411111",
        "CardLastFour": "1111",
        "CardExpDate": "11/25",
        "CardType": "Visa",
        "CardProduct": "C",
        "CardCategory": "Visa Signature (Signature)",
        "EscrowAccumulationId": None,
        "IssuerBankCountry": "RU",
        "Issuer": "CloudPayments",
        "CardTypeCode": 0,
        "Status": "Authorized",
        "StatusCode": 2,
        "CultureName": "ru",
        "Reason": "Approved",
        "CardHolderMessage": "Оплата успешно проведена",
        "Type": 0,
        "Refunded": False,
        "Name": "CARDHOLDER NAME",
        "Token": "0a0afb77-8f41-4de2-9524-1057f9695303",
        "SubscriptionId": None,
        "GatewayName": "Test",
        "ApplePay": False,
        "AndroidPay": False,
        "WalletType": "",
        "TotalFee": 0
    }


class TestTransactionSchema:
    """Test case for checking serialization."""

    def test_serialization(self, raw_transaction_response):
        """Check for successful serialization."""
        serialized = TransactionSchema().load(raw_transaction_response)

        assert serialized