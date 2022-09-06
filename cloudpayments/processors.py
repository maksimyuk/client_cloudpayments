
from cloudpayments.base.processors import BaseMethodProcessor
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
            raw_response = await client.post(
                interaction_method=interaction_method,
                url=endpoint_url,
                **ChargeRequestSchema().dump(schema),
            )
        except Exception as e:
            raise

        # Parsing result
        if raw_response['success']:
            return TransactionSchema().load(raw_response['Model'])

        if raw_response['message']:
            return 'Message'

        if raw_response['model']:
            return 'Model'

        return Secure3dAuthenticationSchema().load(raw_response['Model'])
