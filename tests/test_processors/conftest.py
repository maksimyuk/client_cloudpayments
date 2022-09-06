
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
