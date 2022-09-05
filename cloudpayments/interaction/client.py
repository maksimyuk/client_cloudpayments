
from cloudpayments.base.client import AbstractInteractionClient
from cloudpayments.interaction.mixins import BasicAuthorizationMixin, IdempotenceMixin


class CloudPaymentInteractionClient(BasicAuthorizationMixin, IdempotenceMixin, AbstractInteractionClient):
    """Client for interacting with cloudpayments API."""
