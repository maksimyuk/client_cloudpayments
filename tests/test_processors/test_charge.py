
import pytest

from aioresponses import aioresponses

from cloudpayments.error import IncorrectRequestStructureError, PaymentDeclinedError
from cloudpayments.processors import ChargeProcessor


class TestCharge:
    """Test cases for checking charge method."""

    @pytest.mark.asyncio
    async def test_success_process(self, charge_request_serialized, charge_response_success):
        """Check success charge method."""

        with aioresponses() as m:
            m.post(
                'https://api.cloudpayments.ru/payments/charge',
                payload=charge_response_success,
            )

            response = await ChargeProcessor.process(schema=charge_request_serialized, require_confirmation=False)

            # TODO сделать результат ответа в виде десериализованного объекта
            for key in ('reason_code', 'public_id', 'terminal_url'):
                assert key in response.keys()

    @pytest.mark.asyncio
    async def test_process_incorrect_request_structure(self, charge_request_serialized, charge_response_incorrect_request):
        """Check incorrect request structure."""
        with aioresponses() as m:
            m.post(
                'https://api.cloudpayments.ru/payments/charge',
                payload=charge_response_incorrect_request,
            )

            with pytest.raises(IncorrectRequestStructureError):
                await ChargeProcessor.process(schema=charge_request_serialized, require_confirmation=False)

    @pytest.mark.asyncio
    async def test_process_charge_declined(self, charge_request_serialized, charge_response_charge_declined):
        """Check response for charge declined."""
        with aioresponses() as m:
            m.post(
                'https://api.cloudpayments.ru/payments/charge',
                payload=charge_response_charge_declined,
            )

            with pytest.raises(PaymentDeclinedError):
                await ChargeProcessor.process(schema=charge_request_serialized, require_confirmation=False)

    @pytest.mark.asyncio
    async def test_process_secure_3d(self, charge_request_serialized, charge_response_secure_3d):
        """Check response for secure3d."""
        with aioresponses() as m:
            m.post(
                'https://api.cloudpayments.ru/payments/charge',
                payload=charge_response_secure_3d,
            )

            response = await ChargeProcessor.process(schema=charge_request_serialized, require_confirmation=False)

            # TODO сделать результат ответа в виде десериализованного объекта
            for key in ('transaction_id', 'pa_req', 'acs_url'):
                assert key in response.keys()
