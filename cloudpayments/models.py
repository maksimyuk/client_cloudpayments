
from marshmallow import INCLUDE, Schema, fields


class ChargeErrorModelSchema(Schema):
    """Model for error model in response."""
    transaction_id = fields.String(required=True)
    reason_code = fields.String()

    class Meta:
        unknown = INCLUDE


class ChargeResponseSchema(Schema):
    """
    Model for charge method response.
    https://developers.cloudpayments.ru/#oplata-po-kriptogramme
    """
    success = fields.Bool(required=True)
    message = fields.String(default=None)
    model = fields.Nested(ChargeErrorModelSchema, default=None)
