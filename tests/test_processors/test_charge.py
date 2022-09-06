
import aiohttp
import pytest

from unittest.mock import MagicMock

from cloudpayments.processors import ChargeProcessor


@pytest.mark.asyncio
async def test_download():
    mock = aiohttp.ClientSession
    mock.get = MagicMock()
    mock.get.return_value.__aenter__.return_value.status = 200
    mock.get.return_value.__aenter__.return_value.text.return_value = 'test content'

    async with aiohttp.ClientSession() as session:
        async with session.get('http://test.com') as response:
            assert await response.text() == 'test content'


class TestCharge:
    """Test cases for checking charge method."""

    def test_success_process(self, charge_request_serialized):
        """Check success charge method."""
        pass
