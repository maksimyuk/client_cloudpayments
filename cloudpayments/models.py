
from marshmallow import INCLUDE, Schema, fields
from marshmallow_enum import EnumField

from cloudpayments.enum import Currency


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


class TransactionSchema(Schema):
    """Model for successful Transaction response"""

    reason_code = fields.Integer(data_key='ReasonCode', required=True)
    public_id = fields.String(data_key='PublicId')
    terminal_url = fields.URL(data_key='TerminalUrl')
    transaction_id = fields.Integer(data_key='TransactionId', required=True)
    amount = fields.Float(data_key='Amount', required=True)
    currency = EnumField(Currency, data_key='Currency')
    currency_code = fields.Integer(data_key='CurrencyCode')
    payment_amount = fields.Integer(data_key='PaymentAmount')
    payment_currency = EnumField(Currency, data_key='PaymentCurrency')
    payment_currency_code = fields.Integer(data_key='PaymentCurrencyCode')
    invoice_id = fields.String(data_key='InvoiceId')
    account_id = fields.String(data_key='AccountId')
    email = fields.Email(data_key='Email', allow_none=True)
    description = fields.String(data_key='Description')
    json_data = fields.Dict(data_key='JsonData', allow_none=True)
    created_date = fields.DateTime(data_key='CreatedDate', format='timestamp')
    payout_date = fields.DateTime(data_key='PayoutDate', allow_none=True)
    payout_date_iso = fields.DateTime(data_key='PayoutDateIso', allow_none=True)
    payout_amount = fields.Float(data_key='PayoutAmount', allow_none=True)
    created_date_iso = fields.DateTime(data_key='CreatedDateIso')
    auth_date = fields.DateTime(data_key='AuthDate', format='timestamp')
    auth_date_iso = fields.DateTime(data_key='AuthDateIso')
    confirm_date = fields.DateTime(data_key='ConfirmDate', format='timestamp', allow_none=True)
    confirm_date_iso = fields.DateTime(data_key='ConfirmDateIso', allow_none=True)
    auth_code = fields.String(data_key='AuthCode')
    test_mode = fields.Bool(data_key='TestMode')
    rrn = fields.String(data_key='Rrn', allow_none=True)
    original_transaction_id = fields.Integer(data_key='OriginalTransactionId', allow_none=True)
    fall_back_scenario_declined_transaction_id = fields.Integer(data_key='FallBackScenarioDeclinedTransactionId', allow_none=True)
    ip_address = fields.IPv4(data_key='IpAddress')
    ip_country = fields.String(data_key='IpCountry')
    ip_city = fields.String(data_key='IpCity')
    ip_region = fields.String(data_key='IpRegion')
    ip_district = fields.String(data_key='IpDistrict')
    ip_latitude = fields.Number(data_key='IpLatitude')
    ip_longitude = fields.Number(data_key='IpLongitude')
    card_first_six = fields.String(data_key='CardFirstSix')
    card_last_four = fields.String(data_key='CardLastFour')
    card_expiration_date = fields.String(data_key='CardExpDate')
    card_type = fields.String(data_key='CardType')
    card_product = fields.String(data_key='CardProduct')
    card_category = fields.String(data_key='CardCategory')
    escrow_accumulation_id = fields.Integer(data_key='EscrowAccumulationId', allow_none=True)
    issuer_bank_country = fields.String(data_key='IssuerBankCountry')
    issuer = fields.String(data_key='Issuer')
    card_type_code = fields.Integer(data_key='CardTypeCode')
    status = fields.String(data_key='Status')
    status_code = fields.Integer(data_key='StatusCode')
    culture_name = fields.String(data_key='CultureName')
    reason = fields.String(data_key='Reason')
    card_holder_message = fields.String(data_key='CardHolderMessage')
    type_ = fields.Integer(data_key='Type')
    refunded = fields.Bool(data_key='Refunded')
    name = fields.String(data_key='Name')
    token = fields.String(data_key='Token')
    subscription_id = fields.Integer(data_key='SubscriptionId', allow_none=True)
    gateway_name = fields.String(data_key='GatewayName')
    apple_pay = fields.Bool(data_key='ApplePay')
    android_pay = fields.Bool(data_key='AndroidPay')
    wallet_type = fields.String(data_key='WalletType')
    total_fee = fields.Float(data_key='TotalFee')
