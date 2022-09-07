
from cloudpayments.base.error import BaseInteractionError


class IncorrectRequestStructureError(BaseInteractionError):
    """Error for incorrect structure of request."""

    default_message = 'Incorrect request structure'
