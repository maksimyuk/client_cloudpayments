
import pytest

from aioresponses import aioresponses

from cloudpayments.client import CloudPayment


class TestClient:

    @pytest.mark.asyncio
    async def test_charge(self):
        with aioresponses() as m:
            m.post(
                'https://api.cloudpayments.ru/payments/charge',
                payload={'Success': True},
            )

            with pytest.raises(KeyError):
                await CloudPayment.charge(
                    amount=1,
                    ip_address='1.1.1.1',
                    card_cryptogram_packet='1234',
                )
