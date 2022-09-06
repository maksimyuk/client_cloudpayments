
from aiohttp import BasicAuth

from cloudpayments.interaction.client import CloudPaymentInteractionClient


class TestCloudPaymentInteractionClientSession:
    """Tests for checking cloudpayment client session params."""

    def test_create_client_session(self):
        """Check for params of created client session."""
        session = CloudPaymentInteractionClient().create_session()

        assert session

        # check for auth
        assert isinstance(session.auth, BasicAuth)

        # check for X-Request-ID header
        assert 'X-Request-ID' in session.headers
