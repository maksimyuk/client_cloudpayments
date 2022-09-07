
from cloudpayments.base.error import InteractionResponseError
from cloudpayments.base.processors import BaseMethodProcessor
from cloudpayments.error import IncorrectRequestStructureError
from cloudpayments.interaction.client import CloudPaymentInteractionClient
from cloudpayments.models import ChargeRequestSchema, Secure3dAuthenticationSchema, TransactionSchema


class ChargeProcessor(BaseMethodProcessor):
    """
    Class for processing charge method request.
    https://developers.cloudpayments.ru/#oplata-po-kriptogramme
    """

    async def process(self, schema: ChargeRequestSchema, require_confirmation: bool):
        """Process payment by cryptogram."""
        client = CloudPaymentInteractionClient()

        # Building url for request
        interaction_method = ('auth' if require_confirmation else 'charge')
        relative_url = f'payments/cards/{interaction_method}'
        endpoint_url = client.endpoint_url(relative_url)

        # Making request
        try:
            response = await client.post(
                interaction_method=interaction_method,
                url=endpoint_url,
                json=ChargeRequestSchema().dump(schema),
            )
        except InteractionResponseError as e:
            raise InteractionResponseError(
                status_code=e.status_code, method=e.method, service=e.service
            ) from e
        except Exception as e:
            raise

        # Parsing result
        if response['Success']:
            return TransactionSchema().load(response['Model'])

        if response['Message']:
            raise IncorrectRequestStructureError(
                method="POST",
                service='test',
                message=response['Message'],
            )

        if response['Model']:
            return 'Model'

        return Secure3dAuthenticationSchema().load(response['Model'])
