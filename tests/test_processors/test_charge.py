
import pytest

from aioresponses import aioresponses

from cloudpayments.processors import ChargeProcessor
from cloudpayments.models import TransactionSchema


class TestCharge:
    """Test cases for checking charge method."""

    @pytest.mark.asyncio
    async def test_success_process(self, charge_request_serialized, charge_response_success):
        """Check success charge method."""

        with aioresponses() as m:
            m.post(
                'https://api.cloudpayments.ru/payments/cards/charge',
                payload=charge_response_success,
            )

            response = await ChargeProcessor().process(schema=charge_request_serialized, require_confirmation=False)

            # TODO сделать результат ответа в виде десериализованного объекта
            for key in ('reason_code', 'public_id', 'terminal_url'):
                assert key in response.keys()
