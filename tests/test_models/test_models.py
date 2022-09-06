import pytest

from cloudpayments.models import Secure3dAuthenticationSchema


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