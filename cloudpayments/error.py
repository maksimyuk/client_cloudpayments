
from cloudpayments.base.error import BaseInteractionError


class IncorrectRequestStructureError(BaseInteractionError):
    """Error for incorrect structure of request."""

    default_message = 'Incorrect request structure'


class PaymentDeclinedError(BaseInteractionError):
    """Error for declined payment."""

    default_message = 'Payment declined'

    def __init__(
            self, *, service: str, method: str, reason: str, reason_code: int, cardholder_message: str,
            transaction_id: int, message = None
    ):
        super().__init__(service=service, method=method, message=message)
        self.reason = reason
        self.reason_code = reason_code
        self.cardholder_message = cardholder_message
        self.transaction_id = transaction_id
        self.message = message
