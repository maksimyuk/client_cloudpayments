
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


class ChargeRequestSchema(Schema):
    """Model for charge request."""


class Secure3dAuthenticationSchema(Schema):
    """Model for 3-D secure authentication response."""

    transaction_id = fields.Integer(data_key='TransactionId', required=True)
    pa_req = fields.String(data_key='PaReq', required=True)
    go_req = fields.String(data_key='GoReq', allow_none=True)
    acs_url = fields.URL(data_key='AcsUrl', required=True)
    three_ds_session_data = fields.URL(data_key='ThreeDsSessionData', allow_none=True)
    iframe_is_allowed = fields.Bool(data_key='IFrameIsAllowed')
    frame_width = fields.Integer(data_key='FrameWidth', allow_none=True)
    frame_height = fields.Integer(data_key='FrameHeight', allow_none=True)
    three_ds_session_callback_id = fields.String(data_key='ThreeDsCallbackId')
    escrow_accumulation_id = fields.String(data_key='EscrowAccumulationId', allow_none=True)
