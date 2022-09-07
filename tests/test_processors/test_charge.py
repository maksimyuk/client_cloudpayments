
import aiohttp
import aresponses
import pytest

from cloudpayments.processors import ChargeProcessor


class TestCharge:
    """Test cases for checking charge method."""

    @pytest.mark.asyncio
    async def test_success_process(self, charge_request_serialized, aresponses):
        """Check success charge method."""
        # aresponses.add('api.cloudpayments.ru', 'payments/cards/charge/', 'POST', response='OK')

        response = await ChargeProcessor().process(schema=charge_request_serialized, require_confirmation=False)

        assert response

    @pytest.mark.asyncio
    async def test_ya(self):
       session = aiohttp.ClientSession()

       response = await session.request('POST', 'https://api.cloudpayments.ru/payments/cards/charge')

       assert response
