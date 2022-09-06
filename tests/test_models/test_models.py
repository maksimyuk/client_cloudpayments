import pytest

from cloudpayments.models import ChargeRequestSchema, Secure3dAuthenticationSchema, TransactionSchema


class TestSecure3dAuthenticationSchema:
    """Test case for checking serialization."""

    def test_serialization(self, raw_secure_3d_response):
        """Check for successful serialization."""
        serialized = Secure3dAuthenticationSchema().load(raw_secure_3d_response)

        assert serialized


class TestTransactionSchema:
    """Test case for checking serialization."""

    def test_serialization(self, raw_transaction_response):
        """Check for successful serialization."""
        serialized = TransactionSchema().load(raw_transaction_response)

        assert serialized


class TestChargeRequest:
    """Test case for checking serialization."""

    def test_serialization(self, raw_charge_request):
        """Check for successful serialization."""
        serialized = ChargeRequestSchema().load(raw_charge_request)

        assert serialized
