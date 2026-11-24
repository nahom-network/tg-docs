# RefundedPayment

Source: https://core.telegram.org/bots/api#refundedpayment

[Documentation index](../llms.txt)

This object contains basic information about a refunded payment.

| Field | Type | Description |
| --- | --- | --- |
| currency | String | Three-letter ISO 4217 [currency](../external/bots/payments.md#supported-currencies) code, or “XTR” for payments in [Telegram Stars](https://t.me/BotNews/90). Currently, always “XTR”. |
| total\_amount | Integer | Total refunded price in the *smallest units* of the currency (integer, **not** float/double). For example, for a price of `US$ 1.45`, `total_amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). |
| invoice\_payload | String | Bot-specified invoice payload |
| telegram\_payment\_charge\_id | String | Telegram payment identifier |
| provider\_payment\_charge\_id | String | *Optional*. Provider payment identifier |
